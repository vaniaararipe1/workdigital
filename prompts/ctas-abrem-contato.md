# Prompt: Todos os CTAs de contato da home abrem o painel de contato

Feito a partir da versão publicada em https://workdigital-hero-preview.onrender.com/, testada no navegador:
- **SOLICITAR PROPOSTA** (menu): abre o painel.
- **SOLICITE UMA PROPOSTA** (Soluções): abre o painel.
- **ENTRE EM CONTATO** (rodapé): abre o painel.
- **SOLICITE PROPOSTA** (Transformação digital): **sai do site** e vai para workdigital.art.br/contato/.

## PROMPT (copie daqui para baixo)

Faça **todos os botões de contato da home abrirem o painel de contato do menu** (o mesmo que abre
em SOLICITAR PROPOSTA). **Não altere nada** no visual nem na animação do painel e do menu, nem em
qualquer outra parte do site. A mudança é só em qual botão abre o painel.

### O problema
- O botão **SOLICITE PROPOSTA** da seção Transformação digital (`.wd-transformacao-cta`) tem um
  `addEventListener('click', ...)` próprio no `index.html`, com o comentário *"Honor #contato once
  it exists; until then use Work's real contact page."*.
- Esse código faz `location.assign('https://workdigital.art.br/contato/')`, então o usuário sai do
  site em vez de ver o painel.
- **Remova esse listener inteiro.**

### Deixar explícito quais botões abrem o contato
1. Adicione o atributo `data-wd-contact` nestes botões:
   - `.nav-cta` (SOLICITAR PROPOSTA, no menu);
   - o CTA de contato do menu do celular;
   - `.wd-explore-cta` (SOLICITE UMA PROPOSTA, em Soluções);
   - `.wd-transformacao-cta` (SOLICITE PROPOSTA, em Transformação digital);
   - `.wd-footer-cta` (ENTRE EM CONTATO, no rodapé, gerado no `footer.js`).
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

### Comportamento ao abrir a partir de um botão no meio da página
- O painel continua saindo **de dentro do menu**, exatamente como hoje, sem mudar a posição nem a
  animação.
- Se o menu estiver escondido pela rolagem, mostre o menu primeiro e só então abra o painel.
- A página **não pode pular** de posição ao abrir nem ao fechar.
- Ao fechar, o foco volta para o botão que abriu o painel (a variável `opener` já faz isso; só
  confirme que funciona para todos os botões acima).
- No celular, todos esses botões abrem a mesma versão de tela cheia que já existe.

### Conferir no final
Teste cada botão no computador e no celular e me diga, em uma linha cada, se abre o painel sem
sair da página:
- menu;
- menu do celular;
- Soluções;
- Transformação digital;
- rodapé.

Não altere nenhum outro arquivo ou estilo.
