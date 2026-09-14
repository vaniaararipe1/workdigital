#!/usr/bin/env python3
"""
Interface grafica do Gerador de Propostas Comerciais - Work Digital.

Permite escolher o modelo (simples ou completo), preencher os campos do
cliente em um formulario e gerar o PPTX + PDF prontos, sem tocar em
nenhum arquivo manualmente.
"""
from __future__ import annotations

import subprocess
import sys
import threading
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk

APP_DIR = Path(__file__).resolve().parent
ROOT = APP_DIR.parent if not getattr(sys, "_MEIPASS", None) else Path(sys._MEIPASS)
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

import gerar_proposta as gp  # noqa: E402
from preview import SlidePreview  # noqa: E402

# --------------------------------------------------------------------------- #
# Identidade visual Work Digital
# --------------------------------------------------------------------------- #
ROXO = "#6025E1"
ROXO_ESCURO = "#4A1CB0"
PRETO = "#0B0B0F"
CINZA_ESCURO = "#17171D"
CINZA_MEDIO = "#2A2A33"
BRANCO = "#FFFFFF"
CINZA_CLARO = "#B8B8C4"
VERDE = "#04CD8F"
VERMELHO = "#FF5A5A"

FONTE_TITULO = ("Segoe UI", 15, "bold")
FONTE_LABEL = ("Segoe UI", 10, "bold")
FONTE_TEXTO = ("Segoe UI", 10)
FONTE_AJUDA = ("Segoe UI", 8)


def abrir_no_sistema(caminho: Path) -> None:
    try:
        if sys.platform.startswith("win"):
            import os

            os.startfile(caminho)  # type: ignore[attr-defined]
        elif sys.platform == "darwin":
            subprocess.run(["open", str(caminho)], check=False)
        else:
            subprocess.run(["xdg-open", str(caminho)], check=False)
    except Exception as e:
        messagebox.showerror("Erro ao abrir", str(e))


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Work Digital — Gerador de Propostas")
        self.geometry("1180x780")
        self.minsize(980, 600)
        self.configure(bg=PRETO)
        self._set_icon()

        self.tipo_var = tk.StringVar(value="simples")
        self.pasta_saida = tk.StringVar(value=str(gp.PASTA_SAIDA_PADRAO))
        self.widgets_campos: dict[str, tuple[dict, tk.Widget]] = {}
        self.ultimo_resultado: gp.ResultadoGeracao | None = None

        self._montar_estilo()
        self._montar_header()

        corpo = tk.Frame(self, bg=PRETO)
        corpo.pack(fill="both", expand=True)
        self.coluna_esquerda = tk.Frame(corpo, bg=PRETO)
        self.coluna_esquerda.pack(side="left", fill="both", expand=True)
        self.coluna_direita = tk.Frame(corpo, bg=PRETO, width=480)
        self.coluna_direita.pack(side="right", fill="y", padx=(0, 20), pady=16)

        self._montar_seletor_tipo()
        self._montar_area_formulario()
        self._montar_rodape()
        self._montar_preview()

        self._aviso_libreoffice()
        self._montar_formulario("simples")

    # ----------------------------------------------------------------- #
    def _set_icon(self) -> None:
        try:
            icon_path = ROOT / "assets" / "icon.png"
            if icon_path.exists():
                img = tk.PhotoImage(file=str(icon_path))
                self.iconphoto(True, img)
                self._icon_ref = img
        except Exception:
            pass

    def _montar_estilo(self) -> None:
        style = ttk.Style(self)
        try:
            style.theme_use("clam")
        except Exception:
            pass
        style.configure("TFrame", background=PRETO)
        style.configure("Cinza.TFrame", background=CINZA_ESCURO)
        style.configure(
            "TLabel", background=PRETO, foreground=BRANCO, font=FONTE_TEXTO
        )
        style.configure(
            "Cinza.TLabel", background=CINZA_ESCURO, foreground=BRANCO, font=FONTE_TEXTO
        )
        style.configure(
            "Ajuda.TLabel",
            background=CINZA_ESCURO,
            foreground=CINZA_CLARO,
            font=FONTE_AJUDA,
        )
        style.configure(
            "Titulo.TLabel",
            background=ROXO,
            foreground=BRANCO,
            font=FONTE_TITULO,
        )
        style.configure(
            "Roxo.TRadiobutton",
            background=PRETO,
            foreground=BRANCO,
            font=("Segoe UI", 11, "bold"),
        )
        style.map(
            "Roxo.TRadiobutton",
            foreground=[("selected", ROXO), ("!selected", CINZA_CLARO)],
        )
        style.configure(
            "Gerar.TButton",
            background=ROXO,
            foreground=BRANCO,
            font=("Segoe UI", 12, "bold"),
            padding=12,
            borderwidth=0,
        )
        style.map("Gerar.TButton", background=[("active", ROXO_ESCURO)])
        style.configure(
            "Secundario.TButton",
            background=CINZA_MEDIO,
            foreground=BRANCO,
            font=("Segoe UI", 9, "bold"),
            padding=8,
            borderwidth=0,
        )
        style.map("Secundario.TButton", background=[("active", "#3A3A46")])
        style.configure(
            "TEntry",
            fieldbackground=CINZA_MEDIO,
            foreground=BRANCO,
            insertcolor=BRANCO,
            borderwidth=0,
        )

    def _montar_header(self) -> None:
        header = tk.Frame(self, bg=ROXO)
        header.pack(fill="x", side="top")
        try:
            banner_path = ROOT / "assets" / "logo_banner.png"
            self._banner_img = tk.PhotoImage(file=str(banner_path))
            tk.Label(header, image=self._banner_img, bg=ROXO).pack(
                side="left", padx=20, pady=14
            )
        except Exception:
            tk.Label(
                header, text="work digital", bg=ROXO, fg=BRANCO, font=FONTE_TITULO
            ).pack(side="left", padx=20, pady=14)
        tk.Label(
            header,
            text="Gerador de Propostas Comerciais",
            bg=ROXO,
            fg=BRANCO,
            font=FONTE_TITULO,
        ).pack(side="left", padx=(0, 20))

        self.label_aviso = tk.Label(
            self,
            text="",
            bg="#3A2A00",
            fg="#FFC24B",
            font=FONTE_AJUDA,
            anchor="w",
            justify="left",
            wraplength=1100,
        )

    def _aviso_libreoffice(self) -> None:
        if gp.localizar_soffice() is None:
            self.label_aviso.config(
                text=(
                    "⚠ LibreOffice não foi encontrado neste computador. Você ainda pode "
                    "gerar o PPTX normalmente, mas o PDF não será criado automaticamente. "
                    "Instale gratuitamente em libreoffice.org/download e reabra o programa."
                )
            )
            self.label_aviso.pack(fill="x", padx=0, pady=(0, 4))

    def _montar_seletor_tipo(self) -> None:
        frame = tk.Frame(self.coluna_esquerda, bg=PRETO)
        frame.pack(fill="x", padx=20, pady=(16, 6))

        tk.Label(
            frame, text="Modelo da proposta:", bg=PRETO, fg=BRANCO, font=FONTE_LABEL
        ).pack(side="left", padx=(0, 12))

        ttk.Radiobutton(
            frame,
            text="Simples",
            value="simples",
            variable=self.tipo_var,
            style="Roxo.TRadiobutton",
            command=lambda: self._montar_formulario("simples"),
        ).pack(side="left", padx=6)
        ttk.Radiobutton(
            frame,
            text="Completa",
            value="completa",
            variable=self.tipo_var,
            style="Roxo.TRadiobutton",
            command=lambda: self._montar_formulario("completa"),
        ).pack(side="left", padx=6)

    def _montar_area_formulario(self) -> None:
        container = tk.Frame(self.coluna_esquerda, bg=PRETO)
        container.pack(fill="both", expand=True, padx=20, pady=6)

        canvas = tk.Canvas(container, bg=PRETO, highlightthickness=0)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        self.form_frame = tk.Frame(canvas, bg=PRETO)

        self.form_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=self.form_frame, anchor="nw", width=640)
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        canvas.bind_all(
            "<Button-4>", lambda e: canvas.yview_scroll(-2, "units")
        )
        canvas.bind_all(
            "<Button-5>", lambda e: canvas.yview_scroll(2, "units")
        )

    def _montar_rodape(self) -> None:
        rodape = tk.Frame(self.coluna_esquerda, bg=PRETO)
        rodape.pack(fill="x", padx=20, pady=14)

        linha_pasta = tk.Frame(rodape, bg=PRETO)
        linha_pasta.pack(fill="x", pady=(0, 10))
        tk.Label(
            linha_pasta, text="Salvar em:", bg=PRETO, fg=CINZA_CLARO, font=FONTE_AJUDA
        ).pack(side="left")
        tk.Label(
            linha_pasta,
            textvariable=self.pasta_saida,
            bg=PRETO,
            fg=CINZA_CLARO,
            font=FONTE_AJUDA,
        ).pack(side="left", padx=6)
        ttk.Button(
            linha_pasta,
            text="Alterar pasta…",
            style="Secundario.TButton",
            command=self._escolher_pasta,
        ).pack(side="left", padx=8)

        self.status_var = tk.StringVar(value="")
        self.status_label = tk.Label(
            rodape,
            textvariable=self.status_var,
            bg=PRETO,
            fg=CINZA_CLARO,
            font=FONTE_TEXTO,
            wraplength=620,
            justify="left",
        )
        self.status_label.pack(fill="x", pady=(0, 8))

        linha_botoes = tk.Frame(rodape, bg=PRETO)
        linha_botoes.pack(fill="x")

        self.botao_gerar = ttk.Button(
            linha_botoes,
            text="Gerar proposta",
            style="Gerar.TButton",
            command=self._gerar,
        )
        self.botao_gerar.pack(side="left")

        self.botao_pasta = ttk.Button(
            linha_botoes,
            text="Abrir pasta",
            style="Secundario.TButton",
            command=self._abrir_pasta_resultado,
            state="disabled",
        )
        self.botao_pasta.pack(side="left", padx=8)

        self.botao_pdf = ttk.Button(
            linha_botoes,
            text="Abrir PDF",
            style="Secundario.TButton",
            command=self._abrir_pdf_resultado,
            state="disabled",
        )
        self.botao_pdf.pack(side="left")

    def _montar_preview(self) -> None:
        self.preview = SlidePreview(self.coluna_direita)
        self.preview.pack(anchor="n")

    def _atualizar_preview(self, *_args) -> None:
        if hasattr(self, "preview"):
            self.preview.definir_valores(self._coletar_dados())

    def _escolher_pasta(self) -> None:
        pasta = filedialog.askdirectory(initialdir=self.pasta_saida.get())
        if pasta:
            self.pasta_saida.set(pasta)

    # ----------------------------------------------------------------- #
    # Formulario dinamico, a partir do schema JSON (mesma fonte usada pelo
    # gerador de linha de comando — nao ha lista de campos duplicada aqui).
    # ----------------------------------------------------------------- #
    def _montar_formulario(self, tipo: str) -> None:
        for w in self.form_frame.winfo_children():
            w.destroy()
        self.widgets_campos.clear()
        self.botao_pasta.config(state="disabled")
        self.botao_pdf.config(state="disabled")
        self.status_var.set("")

        schema = gp.carregar_schema(tipo)
        self.preview.carregar(ROOT / schema["template"], schema)

        linha_data = tk.Frame(self.form_frame, bg=PRETO)
        linha_data.pack(fill="x", pady=(4, 14))
        tk.Label(
            linha_data, text="Data da proposta", bg=PRETO, fg=BRANCO, font=FONTE_LABEL
        ).pack(anchor="w")
        import datetime

        self.data_entry = ttk.Entry(linha_data, width=16, font=FONTE_TEXTO)
        self.data_entry.insert(0, datetime.date.today().strftime("%d-%m-%Y"))
        self.data_entry.pack(anchor="w", pady=(4, 0))

        for campo in schema["campos"]:
            self._montar_campo(campo)

        self._atualizar_preview()

    def _montar_campo(self, campo: dict) -> None:
        bloco = tk.Frame(self.form_frame, bg=PRETO)
        bloco.pack(fill="x", pady=8)

        titulo = campo["descricao"]
        if campo.get("obrigatorio"):
            titulo += "  *"
        tk.Label(bloco, text=titulo, bg=PRETO, fg=BRANCO, font=FONTE_LABEL).pack(
            anchor="w"
        )

        tipo_campo = campo["tipo_campo"]
        padrao = campo.get("padrao")

        if tipo_campo in ("single", "suffix"):
            entry = tk.Entry(
                bloco,
                bg=CINZA_MEDIO,
                fg=BRANCO,
                insertbackground=BRANCO,
                relief="flat",
                font=FONTE_TEXTO,
            )
            if isinstance(padrao, str):
                entry.insert(0, padrao)
            entry.bind("<KeyRelease>", self._atualizar_preview)
            entry.pack(fill="x", ipady=6, pady=(4, 0))
            self.widgets_campos[campo["chave"]] = (campo, entry)
        elif tipo_campo == "image":
            var = tk.StringVar(value="")
            var.trace_add("write", self._atualizar_preview)
            linha = tk.Frame(bloco, bg=PRETO)
            linha.pack(fill="x", pady=(4, 0))

            def escolher(v=var):
                caminho = filedialog.askopenfilename(
                    title="Escolher logo do cliente",
                    filetypes=[("Imagens", "*.png *.jpg *.jpeg")],
                )
                if caminho:
                    v.set(caminho)

            ttk.Button(
                linha,
                text="Escolher logo…",
                style="Secundario.TButton",
                command=escolher,
            ).pack(side="left")
            tk.Label(
                linha,
                textvariable=var,
                bg=PRETO,
                fg=CINZA_CLARO,
                font=FONTE_AJUDA,
                anchor="w",
            ).pack(side="left", padx=8, fill="x", expand=True)
            self.widgets_campos[campo["chave"]] = (campo, var)
        else:  # multiline / multiline_com_titulo
            dica = "Uma linha por item. Comece cada item com \"- \" se fizer sentido."
            tk.Label(
                bloco, text=dica, bg=PRETO, fg=CINZA_CLARO, font=FONTE_AJUDA
            ).pack(anchor="w", pady=(2, 0))
            text = tk.Text(
                bloco,
                height=4,
                bg=CINZA_MEDIO,
                fg=BRANCO,
                insertbackground=BRANCO,
                relief="flat",
                font=FONTE_TEXTO,
                wrap="word",
            )
            if isinstance(padrao, list):
                text.insert("1.0", "\n".join(padrao))
            text.bind("<KeyRelease>", self._atualizar_preview)
            text.pack(fill="x", pady=(4, 0))
            self.widgets_campos[campo["chave"]] = (campo, text)

    # ----------------------------------------------------------------- #
    def _coletar_dados(self) -> dict:
        dados: dict = {"data": self.data_entry.get().strip()}
        for chave, (campo, widget) in self.widgets_campos.items():
            if isinstance(widget, tk.Text):
                linhas = [
                    l.strip()
                    for l in widget.get("1.0", "end").splitlines()
                    if l.strip()
                ]
                dados[chave] = linhas
            else:
                dados[chave] = widget.get().strip()
        return dados

    def _gerar(self) -> None:
        tipo = self.tipo_var.get()
        dados = self._coletar_dados()
        saida_dir = Path(self.pasta_saida.get())

        self.botao_gerar.config(state="disabled")
        self.botao_pasta.config(state="disabled")
        self.botao_pdf.config(state="disabled")
        self.status_var.set("Gerando proposta, aguarde…")
        self.status_label.config(fg=CINZA_CLARO)

        def trabalho():
            try:
                resultado = gp.gerar(tipo, dados, saida_dir)
                self.after(0, self._ao_concluir_sucesso, resultado)
            except gp.DadosInvalidos as e:
                self.after(0, self._ao_concluir_erro, str(e))
            except Exception as e:  # pragma: no cover - defensivo
                self.after(0, self._ao_concluir_erro, f"Erro inesperado: {e}")

        threading.Thread(target=trabalho, daemon=True).start()

    def _ao_concluir_sucesso(self, resultado: gp.ResultadoGeracao) -> None:
        self.ultimo_resultado = resultado
        self.botao_gerar.config(state="normal")
        self.botao_pasta.config(state="normal")

        partes = [f"✔ PPTX gerado: {resultado.pptx_path.name}"]
        if resultado.pdf_path:
            partes.append(f"✔ PDF gerado: {resultado.pdf_path.name}")
            self.botao_pdf.config(state="normal")
        if resultado.aviso:
            partes.append(f"⚠ {resultado.aviso}")
        self.status_label.config(fg=VERDE if resultado.pdf_path else "#FFC24B")
        self.status_var.set("\n".join(partes))

    def _ao_concluir_erro(self, mensagem: str) -> None:
        self.botao_gerar.config(state="normal")
        self.status_label.config(fg=VERMELHO)
        self.status_var.set(f"✖ {mensagem}")
        messagebox.showerror("Não foi possível gerar a proposta", mensagem)

    def _abrir_pasta_resultado(self) -> None:
        if self.ultimo_resultado:
            abrir_no_sistema(self.ultimo_resultado.pptx_path.parent)

    def _abrir_pdf_resultado(self) -> None:
        if self.ultimo_resultado and self.ultimo_resultado.pdf_path:
            abrir_no_sistema(self.ultimo_resultado.pdf_path)


def main() -> None:
    App().mainloop()


if __name__ == "__main__":
    main()
