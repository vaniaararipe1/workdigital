# Como ligar o popup do RD Station e a landing à página do diagnóstico

A página do diagnóstico fica em **https://diagnostico.workdigital.art.br**. Ela aceita os dados do lead de duas formas e já mostra o site preenchido, com o botão **"Pegue seu relatório"**:

1. **Pelo endereço (recomendado para a landing):**
   ```
   https://diagnostico.workdigital.art.br/?origem=landing&site=SITE&email=EMAIL&nome=NOME&whatsapp=WHATSAPP&segmento=SEGMENTO&cargo=CARGO
   ```
   Cada valor precisa estar codificado para URL (o `encodeURIComponent` do JavaScript faz isso).
2. **Por um cookie `wd_lead`** gravado no domínio `.workdigital.art.br` (recomendado para o popup do RD Station). Ele não depende do RD conseguir levar os campos no redirecionamento.

Quando a página recebe **site e e-mail**, ela esconde os outros campos e mostra só o site e o botão. Ela parte do princípio de que o consentimento já foi dado no formulário anterior, então **os dois formulários precisam ter o texto de consentimento**.

Depois de ler os dados, a página apaga o cookie e limpa o endereço, para o e-mail não ficar no histórico do navegador.

---

## Cenário 1: popup do RD Station no site da Work Digital (WordPress)

**Passo 1. No RD Station**, no pop-up:
- inclua o campo do site, por exemplo um campo personalizado "Site";
- em "Após a conversão", escolha **redirecionar para a URL** `https://diagnostico.workdigital.art.br/?origem=popup`.

**Passo 2. No WordPress**, cole o código abaixo no rodapé do site. Use um plugin como "WPCode" ou "Insert Headers and Footers", na área do rodapé. O código lê os campos do pop-up no momento do envio e grava o cookie que a página do diagnóstico vai ler.

```html
<script>
/* Work Digital · leva os dados do pop-up do RD Station para a página do diagnóstico */
(function () {
  function achar(dados, chaves) {
    for (var k in dados) {
      var nome = k.toLowerCase();
      for (var i = 0; i < chaves.length; i++) if (nome.indexOf(chaves[i]) !== -1 && dados[k]) return dados[k];
    }
    return "";
  }
  document.addEventListener("submit", function (ev) {
    var form = ev.target;
    if (!form || !form.querySelector) return;
    var dados = {};
    new FormData(form).forEach(function (v, k) { if (typeof v === "string") dados[k] = v.trim(); });
    var email = achar(dados, ["email"]);
    var site = achar(dados, ["site", "url", "website", "endereco"]);
    if (!email || !site) return; // não é o formulário do diagnóstico
    var lead = {
      email: email, site: site,
      nome: achar(dados, ["name", "nome"]),
      whatsapp: achar(dados, ["whats", "phone", "celular", "telefone", "mobile"]),
      empresa: achar(dados, ["company", "empresa"]),
      origem: "popup"
    };
    document.cookie = "wd_lead=" + encodeURIComponent(JSON.stringify(lead)) +
      "; Max-Age=900; path=/; domain=.workdigital.art.br; Secure; SameSite=Lax";
  }, true);
})();
</script>
```

**Passo 3. Teste:**
1. Preencha o pop-up com um e-mail seu e o site de teste.
2. Você deve cair na página do diagnóstico com o site já preenchido.
3. Se o campo aparecer vazio, o nome do campo de site no RD é diferente. Me mande o nome que aparece no editor do pop-up que eu ajusto a lista `["site", "url", ...]`.

---

## Cenário 2: landing page em WordPress (feita pelo GPT)

**Opção A. Formulário do RD Station embutido na landing:** use o mesmo código do cenário 1, colado na landing. No RD, configure o redirecionamento para `https://diagnostico.workdigital.art.br/?origem=landing`.

**Opção B. Formulário do próprio WordPress (Elementor, Contact Form 7 ou outro):** depois do envio, redirecione para:
```
https://diagnostico.workdigital.art.br/?origem=landing&site={site}&email={email}&nome={nome}&whatsapp={whatsapp}&segmento={segmento}&cargo={cargo}
```
- **Elementor Pro:** em "Ações após o envio", escolha **Redirecionar** e use os códigos de campo (`[field id="email"]` e assim por diante) no lugar das chaves.
- **Contact Form 7:** cole este código na landing:
```html
<script>
document.addEventListener("wpcf7mailsent", function (ev) {
  var d = {}; (ev.detail.inputs || []).forEach(function (i) { d[i.name] = i.value; });
  var q = new URLSearchParams({ origem: "landing", site: d.site || "", email: d.email || "",
    nome: d.nome || "", whatsapp: d.whatsapp || "", segmento: d.segmento || "", cargo: d.cargo || "" });
  location.href = "https://diagnostico.workdigital.art.br/?" + q.toString();
});
</script>
```
Troque `d.site`, `d.email` e os demais pelos nomes dos campos do seu formulário, se forem outros.

**Texto para o GPT ajustar a landing:** "Depois do envio do formulário, redirecione para https://diagnostico.workdigital.art.br/ com os parâmetros origem=landing, site, email, nome, whatsapp, segmento e cargo, todos codificados para URL. O formulário precisa manter o texto de consentimento."

---

## Cenário 3: prospecção feita pela Vania

Sem nenhuma tela antes. Escolha uma das opções:
- **Pelo GitHub:**
  1. Abra o repositório `workdigital-diagnosticos`, vá em **Actions**, escolha **Diagnóstico automático** e clique em **Run workflow**.
  2. Preencha site, empresa e, se quiser, o e-mail do lead. Funciona no celular.
  3. O relatório chega no seu e-mail. Ele só vai para o lead se você marcar "Enviar a versão automática ao lead agora".
- **Pela página:** abra https://diagnostico.workdigital.art.br sem parâmetros e preencha.
- **Pelo Claude:** peça "rode o diagnóstico de site.com.br para a Empresa X".
