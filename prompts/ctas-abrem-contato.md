# Prompt: Todos os CTAs de contato da home abrem o painel de contato

Feito a partir da versão publicada em https://workdigital-hero-preview.onrender.com/, testada no navegador:
- **SOLICITAR PROPOSTA** (menu): abre o painel.
- **SOLICITE UMA PROPOSTA** (Soluções): abre o painel.
- **ENTRE EM CONTATO** (rodapé): abre o painel.
- **SOLICITE PROPOSTA** (Transformação digital): **sai do site** e vai para workdigital.art.br/contato/.

## PROMPT (copie daqui para baixo)

Faça **todos os botões de contato da home abrirem o painel de contato do menu**, o mesmo que abre
ao clicar em SOLICITAR PROPOSTA. São 5 botões:
1. **SOLICITAR PROPOSTA**, no menu (`.nav-cta`).
2. O botão de contato do **menu do celular**.
3. **SOLICITE UMA PROPOSTA**, na seção Soluções (`.wd-explore-cta`).
4. **SOLICITE PROPOSTA**, na seção **Transformação digital** (`.wd-transformacao-cta`).
5. **ENTRE EM CONTATO**, no rodapé (`.wd-footer-cta`, gerado no `footer.js`).

**Não altere nada** no visual nem na animação do painel e do menu, nem em qualquer outra parte do
site. A mudança é só em qual botão abre o painel.

### 1. Corrigir o CTA da Transformação digital (o mais importante)
- Hoje, o botão **SOLICITE PROPOSTA** da seção Transformação digital (`.wd-transformacao-cta`)
  **leva o usuário para fora do site** em vez de abrir o painel.
- A causa é um `addEventListener('click', ...)` próprio desse botão no `index.html`, com o
  comentário *"Honor #contato once it exists; until then use Work's real contact page."*. Esse
  código faz `location.assign('https://workdigital.art.br/contato/')`.
- **Remova esse listener inteiro.** O resto do script da seção Transformação digital (animação das
  linhas, do título etc.) continua igual.
- Depois da correção, esse botão abre o painel do menu como os outros.

### 2. Marcar todos os botões de contato
1. Adicione o atributo `data-wd-contact` nos 5 botões listados no início, incluindo o
   `.wd-transformacao-cta`.
2. No `contact.js`, junto do listener de clique que já existe, trate também esse atributo:
   ```js
   document.addEventListener('click',e=>{
     const el=e.composedPath().find(n=>n.nodeType===1&&n.hasAttribute&&n.hasAttribute('data-wd-contact'));
     if(!el||el===ctaMenu) return;
     e.preventDefault();
     abrirContato(el);
   });
   ```
   Mantenha o listener atual, que intercepta links para `/contato/` e `#contato`, como garantia.
3. Mantenha o `href` dos links apontando para `https://workdigital.art.br/contato/`. Assim, se o
   JavaScript falhar, o link continua levando para a página de contato. A lógica do
   `data-wd-explore-url` continua como está.

### 3. Comportamento ao abrir a partir de um botão no meio da página
- O painel continua saindo **de dentro do menu**, exatamente como hoje, sem mudar a posição nem a
  animação.
- Se o menu estiver escondido pela rolagem, mostre o menu primeiro e só então abra o painel.
- A página **não pode pular** de posição ao abrir nem ao fechar.
- Ao fechar, o foco volta para o botão que abriu o painel. A variável `opener` já faz isso; só
  confirme que funciona para os 5 botões.
- No celular, todos esses botões abrem a mesma versão de tela cheia que já existe.

### 4. Conferir no final
Teste cada botão no computador e no celular e me diga, em uma linha cada, se abre o painel sem
sair da página:
- menu;
- menu do celular;
- Soluções;
- **Transformação digital**;
- rodapé.

Não altere nenhum outro arquivo ou estilo.
