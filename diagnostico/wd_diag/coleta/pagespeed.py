"""Performance: Google PageSpeed Insights (preferencial) com fallback para Lighthouse local.

O PageSpeed roda o mesmo Lighthouse nos servidores do Google e ainda traz dados de
usuários reais (Chrome UX Report), quando o site tem visitas suficientes.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile

import requests

from ..config import Config

PSI_URL = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
LIGHTHOUSE_VERSAO = "13.5.0"


def chamar_pagespeed(url: str, estrategia: str, config: Config) -> dict:
    if not config.pagespeed_api_key:
        return {"erro": "chave PAGESPEED_API_KEY não configurada"}
    params = {"url": url, "strategy": estrategia, "category": "performance", "locale": "pt_BR",
              "key": config.pagespeed_api_key}
    try:
        r = requests.get(PSI_URL, params=params, timeout=config.timeout_pagespeed)
    except requests.RequestException as e:
        return {"erro": f"PageSpeed indisponível ({type(e).__name__})"}
    if r.status_code != 200:
        try:
            motivo = r.json().get("error", {}).get("message", "")[:200]
        except ValueError:
            motivo = ""
        return {"erro": f"PageSpeed respondeu {r.status_code}. {motivo}".strip()}
    dados = r.json()
    return {"fonte": "pagespeed", "lhr": dados.get("lighthouseResult", {}),
            "campo": dados.get("loadingExperience", {}), "erro": None}


def chamar_lighthouse_local(url: str, estrategia: str, config: Config) -> dict:
    npx = shutil.which("npx")
    if not npx:
        return {"erro": "Lighthouse local indisponível (Node.js não instalado)"}
    with tempfile.TemporaryDirectory() as tmp:
        saida = os.path.join(tmp, "lhr.json")
        cmd = [npx, "--yes", f"lighthouse@{LIGHTHOUSE_VERSAO}", url, "--output=json", f"--output-path={saida}",
               "--quiet", "--only-categories=performance", "--locale=pt-BR",
               "--chrome-flags=--headless=new --no-sandbox --disable-gpu"]
        if estrategia == "desktop":
            cmd.append("--preset=desktop")
        env = dict(os.environ)
        if config.chromium_path:
            env["CHROME_PATH"] = config.chromium_path
        try:
            subprocess.run(cmd, check=True, timeout=config.timeout_pagespeed + 60, env=env,
                           stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
            with open(saida, encoding="utf-8") as f:
                lhr = json.load(f)
        except subprocess.TimeoutExpired:
            return {"erro": "Lighthouse local: tempo esgotado"}
        except (subprocess.CalledProcessError, OSError, ValueError) as e:
            detalhe = getattr(e, "stderr", b"") or b""
            return {"erro": f"Lighthouse local falhou: {detalhe.decode(errors='replace')[-200:].strip() or type(e).__name__}"}
    if lhr.get("runtimeError"):
        return {"erro": f"Lighthouse local: {lhr['runtimeError'].get('message', 'erro')}"}
    return {"fonte": "lighthouse_local", "lhr": lhr, "campo": {}, "erro": None}


def medir(url: str, estrategia: str, config: Config) -> dict:
    """Tenta PageSpeed; se falhar, Lighthouse local. Registra as tentativas."""
    tentativas = []
    r = chamar_pagespeed(url, estrategia, config)
    tentativas.append({"fonte": "pagespeed", "erro": r.get("erro")})
    if r.get("erro") and config.usar_lighthouse_local:
        r = chamar_lighthouse_local(url, estrategia, config)
        tentativas.append({"fonte": "lighthouse_local", "erro": r.get("erro")})
    r["tentativas"] = tentativas
    r["estrategia"] = estrategia
    return r


# ---------------- extração (função pura, testável) ----------------

AUDITS_INTERESSE = (
    "image-delivery-insight", "render-blocking-insight", "document-latency-insight", "font-display-insight",
    "lcp-discovery-insight", "cache-insight", "third-parties-insight", "legacy-javascript-insight",
    "unused-javascript", "unused-css-rules", "uses-optimized-images", "modern-image-formats",
    "uses-responsive-images", "offscreen-images", "render-blocking-resources", "uses-text-compression",
    "server-response-time", "uses-long-cache-ttl", "total-byte-weight", "unminified-javascript",
    "unminified-css", "efficient-animated-content", "duplicated-javascript", "dom-size-insight",
)


def _num(audits: dict, chave: str):
    a = audits.get(chave) or {}
    return a.get("numericValue")


def extrair(resultado: dict) -> dict:
    """Converte a resposta do PageSpeed/Lighthouse no formato usado pela análise."""
    if resultado.get("erro") or not resultado.get("lhr"):
        return {"ok": False, "erro": resultado.get("erro") or "sem resultado",
                "tentativas": resultado.get("tentativas", [])}
    lhr = resultado["lhr"]
    audits = lhr.get("audits", {})
    nota = (lhr.get("categories", {}).get("performance") or {}).get("score")
    campo = (resultado.get("campo") or {}).get("metrics", {}) or {}

    def campo_p75(chave):
        m = campo.get(chave) or {}
        return m.get("percentile")

    inp_campo = campo_p75("INTERACTION_TO_NEXT_PAINT")
    oportunidades = []
    for chave, a in audits.items():
        if chave not in AUDITS_INTERESSE:
            continue
        score = a.get("score")
        if score is None or score >= 0.9:
            continue
        det = a.get("details") or {}
        ms = det.get("overallSavingsMs") or (a.get("metricSavings") or {}).get("LCP") or 0
        bytes_ = det.get("overallSavingsBytes") or 0
        if chave == "total-byte-weight" or (ms <= 0 and bytes_ <= 0):
            continue
        oportunidades.append({"id": chave, "titulo": a.get("title", chave), "economia_ms": round(ms or 0),
                              "economia_bytes": round(bytes_ or 0)})
    oportunidades.sort(key=lambda o: (o["economia_ms"], o["economia_bytes"]), reverse=True)

    return {
        "ok": True,
        "fonte": resultado.get("fonte"),
        "estrategia": resultado.get("estrategia"),
        "versao_lighthouse": lhr.get("lighthouseVersion"),
        "data": lhr.get("fetchTime"),
        "url_final": lhr.get("finalDisplayedUrl") or lhr.get("finalUrl"),
        "nota": round(nota * 100) if isinstance(nota, (int, float)) else None,
        "lcp_ms": _num(audits, "largest-contentful-paint"),
        "fcp_ms": _num(audits, "first-contentful-paint"),
        "cls": _num(audits, "cumulative-layout-shift"),
        "tbt_ms": _num(audits, "total-blocking-time"),
        "bytes_total": _num(audits, "total-byte-weight"),
        "inp_ms_campo": inp_campo,
        "lcp_ms_campo": campo_p75("LARGEST_CONTENTFUL_PAINT_MS"),
        "cls_campo": (campo_p75("CUMULATIVE_LAYOUT_SHIFT_SCORE") / 100) if campo_p75("CUMULATIVE_LAYOUT_SHIFT_SCORE") is not None else None,
        "tem_dados_campo": bool(campo),
        "oportunidades": oportunidades[:6],
        "tentativas": resultado.get("tentativas", []),
    }
