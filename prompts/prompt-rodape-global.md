# Prompt — Rodapé global do site

Referência: rodapé da home de https://www.auros.global/
Anexe um print do rodapé da Auros e o arquivo do logo da Work Digital (de preferência SVG ou PNG
com fundo transparente).

## PROMPT (copie daqui para baixo)

Crie o **rodapé do site da Work Digital**, seguindo **a mesma estrutura visual do rodapé da Auros**
(print em anexo): mesma grade, colunas, proporções, tipografia, espaçamentos, divisórias e hover
dos links. Use as cores da Work Digital e o mesmo padrão das seções que já criamos.

**Este rodapé é global:** vai aparecer em **todas as páginas do site**, não só na home. Entregue
como um componente reutilizável, que eu possa incluir em qualquer página com uma linha só, sem
copiar o código inteiro em cada uma. Por exemplo:
- um arquivo `footer.js` que define um Web Component `<wd-footer></wd-footer>`; ou
- um arquivo `footer.html` carregado por um pequeno script em um `<div id="wd-footer"></div>`.

O CSS do rodapé fica em um arquivo próprio (`footer.css`) ou dentro do componente, com classes
prefixadas `wd-footer-`, para não conflitar com o CSS de nenhuma página.

**Conteúdo (substituições)**

| Na referência | Na Work Digital |
|---|---|
| "Making digital markets liquid" | **Logo da Work Digital em tamanho grande**, ocupando o mesmo espaço que esse texto ocupa na referência (arquivo em anexo; deixe o caminho fácil de trocar, ex.: `img/logo-work-digital.svg`) |
| Texto abaixo dele | **Criação de sites e lojas virtuais de alta performance e focados em conversão.** |
| "Menu" | **Work Digital 2026 © Todos os direitos reservados** |
| "Connect with our team" | **Qual é a sua ideia?** |
| Botão "GET IN TOUCH" | **ENTRE EM CONTATO** (mesmo estilo e hover dos CTAs do site; link para a página de contato) |
| Redes sociais da referência | **Redes sociais da Work Digital** (ver abaixo) |

- O logo tem `alt="Work Digital"` e é um link para a home.
- O ano no texto de direitos é gerado automaticamente com JavaScript
  (`new Date().getFullYear()`), para não ficar desatualizado.

**Redes sociais**
Use os perfis oficiais da Work Digital que aparecem no site atual (https://workdigital.art.br/).
Se não conseguir acessar, deixe os links abaixo para eu preencher:
- Instagram: `[link]`
- LinkedIn: `[link]`
- Facebook: `[link]`
- WhatsApp: `https://wa.me/5511993916363`
- E-mail: `hello@workdigital.art.br`

Use ícones SVG inline (não use imagens nem bibliotecas externas), no mesmo tamanho, cor e hover
dos ícones da referência. Cada ícone tem `aria-label` com o nome da rede e abre em nova aba
(`target="_blank" rel="noopener"`). Remova da lista a rede que eu deixar sem link.

**CSS**
- O rodapé tem o mesmo fundo da referência adaptado às cores da Work. Se a referência não tiver
  fundo próprio, use `background: transparent`, mantendo o gradiente do site contínuo, sem faixas
  entre a última seção e o rodapé.
- Títulos na mesma fonte das seções anteriores; textos de apoio em **Nunito**.
- Responsivo: no tablet as colunas viram 2; no celular ficam empilhadas em 1 coluna, com o logo
  em cima, ocupando a largura disponível, sem rolagem horizontal.
- Links com foco visível no teclado e contraste AA. Use `<footer>` semântico.

Devolva os arquivos completos do rodapé e um exemplo de como incluí-lo em uma página.
