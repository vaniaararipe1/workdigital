# Prompt — Ajustes gerais do site (todas as seções)

Anexe antes de enviar:
- as 3 imagens dos boxes de "Soluções Work" (na ordem: Sites, Blogs, Landing pages);
- os logos das certificações da Work Digital (do site https://workdigital.art.br/);
- prints da seção EXPLORE/Global presence da Auros (e, se possível, o CSS do globo copiado pelo
  DevTools do navegador: botão direito no globo > Inspecionar > copiar os estilos).

## PROMPT (copie daqui para baixo)

Faça os ajustes abaixo no site da Work Digital. Altere **somente** o que está listado, mantendo
todo o resto como está. No final, devolva o código atualizado de cada parte alterada, organizado
pelos mesmos títulos desta lista.

### GERAL (vale para o site inteiro)
1. **Fonte dos descritivos:** todos os textos descritivos (parágrafos, textos de apoio, resumos,
   depoimentos, descrições de cards) devem usar **Nunito** (Google Fonts). Títulos continuam com
   a fonte atual.
2. **Uptitles com degradê:** todas as seções têm um uptitle (ex.: "ACEITE O DESAFIO DO NOVO").
   Aplique em **todos** o mesmo degradê usado nos uptitles da referência (Auros), adaptado às
   cores da Work, e deixe **todos com o mesmo tamanho, peso, `letter-spacing` e caixa**. Crie uma
   classe única (ex.: `.wd-uptitle`) e use em todas as seções.
3. **Descritivos abaixo dos títulos:** todos os textos descritivos logo abaixo dos títulos das
   seções devem ter **o mesmo tamanho** (uma classe única, ex.: `.wd-section-desc`).
4. **Degradê rosa mais iluminado:** o degradê rosa ainda está escuro. Deixe-o mais claro e
   luminoso, no mesmo nível de brilho do degradê roxo.
5. **Frase "Onde você está quando seu cliente NÃO procura por você?":** quebre em **3 linhas** no
   desktop (ex.: "Onde você está / quando seu cliente / NÃO procura por você?"). No celular pode
   quebrar naturalmente.
6. **Botão flutuante de WhatsApp:** adicione um botão flutuante de WhatsApp igual ao do site
   https://videogamesnoabc.com.br/ (mesma posição, formato, tamanho, animação e comportamento;
   se ele abrir uma janelinha de conversa antes de ir para o WhatsApp, faça igual). Ele aparece
   em todas as páginas. Deixe número, mensagem inicial e textos em variáveis no topo do código,
   com valores provisórios (`NUMERO_WHATSAPP`, `MENSAGEM_INICIAL`), que vou te passar depois.

### MENU
1. **Idiomas:** no lugar de "PT / EN", coloque um **seletor de idiomas** (`<select>` estilizado ou
   dropdown) com um **ícone de globo** ao lado, igual ao do site atual da Work Digital
   (https://workdigital.art.br/). Opções: Português e English.
2. **Dropdown SOLUÇÕES:** aumente um pouco o tamanho das fontes dos itens (cerca de 1px a 2px).
3. **Remova "CONTATO"** do menu.
4. **Troque "Cases" por "Work".**
5. **CTA do menu:** o texto passa a ser **SOLICITAR PROPOSTA**.

### HEADER (topo da home)
1. Em **"Criação de sites profissionais"**, aplique o mesmo degradê dos uptitles.
2. Diminua o espaçamento entre o texto "O site da sua empresa precisa..." e a seção seguinte
   ("ACEITE O DESAFIO DO NOVO").

### SOLUÇÕES WORK (`#wd-explore`)
1. Coloque em cada box a imagem correspondente em anexo (Sites, Blogs, Landing pages), no espaço
   de imagem do hover, com `object-fit: cover`.
2. Aplique nas partículas do fundo desta seção **o mesmo efeito** das partículas do fundo dos
   cards dos cases (mesmo movimento, tamanho, densidade e opacidade).
3. Diminua um pouco o espaçamento entre esta seção e a próxima.
4. A cor do hover dos boxes passa a ser **a mesma cor do hover dos cards de artigos do blog**.

### WORKS (`#wd-works`)
1. **Remova o uptitle "CASES".**
2. Deixe o texto descritivo em **2 linhas** no desktop (ajuste a largura máxima do texto).
3. Diminua o espaçamento entre esta seção e a frase "Onde você está quando seu cliente NÃO
   procura por você?". Diminua também o espaçamento entre essa frase e a seção EXPLORE.

### EXPLORE / TRANSFORMAÇÃO DIGITAL (`#wd-transformacao`)
A iluminação ainda está muito diferente da referência (prints e CSS da Auros em anexo).
Deixe **igual à referência**, trocando só o verde-azulado pelas cores da Work:
1. **Fundo do retângulo (card):** reproduza o mesmo degradê e a mesma distribuição de luz da
   referência: escuro na área do texto, clareando em direção ao globo, com a luz do globo se
   espalhando pelo fundo e pela parte de baixo do card.
2. **Remova o degradê reto do globo:** hoje existe uma transição em linha reta (`linear-gradient`
   ou uma camada retangular com blur) que aparece no globo. Use apenas gradientes radiais e
   brilhos que terminam em transparente, sem nenhuma linha reta visível.
3. **Sombras internas do globo:** refaça para ficarem iguais à referência, dando volume e
   profundidade, sem faixas cinzas e sem aparência chapada. Se o CSS da referência estiver em
   anexo, use os mesmos valores (gradientes, `box-shadow`, `filter`, opacidades), trocando só as
   cores.

### FRASE "QUEM NÃO É ENCONTRADO, NÃO É ESCOLHIDO."
1. **Remova essa frase** e, no lugar dela, coloque os **logos das certificações** que aparecem no
   site atual da Work Digital (arquivos em anexo), alinhados em uma linha, com o mesmo tamanho
   visual, em versão clara/monocromática para combinar com o fundo. No celular, quebram em 2 linhas.
2. **Remova também** o texto "Site, blog e landing page trabalhando antes do cliente procurar."

### CONFIANÇA (depoimentos)
1. Remova a **3ª linha** (linha/divisória) que aparece ao lado do 3º depoimento.
2. **Aumente o tamanho dos logos** dos clientes.
3. **Diminua o tamanho da fonte** dos textos dos depoimentos (em Nunito).

### RODAPÉ (global)
1. **Remova o WhatsApp e o e-mail** do rodapé (o WhatsApp passa a ficar no botão flutuante).
2. Troque "Qual é a sua ideia?" por **"Como podemos te ajudar?"** e aumente a fonte desse texto
   em **2px**.
3. O texto de direitos deve ficar exatamente nesta ordem:
   **Work Digital © 2026 | Todos os direitos reservados**
   (o ano continua gerado automaticamente pelo JavaScript). **Diminua** o tamanho da fonte dele.
4. **Aumente** o tamanho da fonte do texto "Criação de sites e lojas virtuais de alta performance
   e focados em conversão."

Ao final, liste em uma linha por item o que foi alterado.
