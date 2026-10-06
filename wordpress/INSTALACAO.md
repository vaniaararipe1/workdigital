# Site da Work Digital no WordPress — instalação

Tudo o que é preciso está nesta pasta (`wordpress/`) e na pasta `site/` do repositório.

| O quê | Onde |
|---|---|
| Tema pronto | `wordpress/theme/workdigital/` (ou `workdigital-tema.zip`) |
| Importador de conteúdo | `wordpress/importar.php` + `wordpress/importacao/conteudo.json` |
| Arquivos importados (artes, thumbs, fotos) | `site/cases/`, `site/thumbs/`, `site/img/blog/`, `site/img/` |
| Redirecionamentos do site antigo | `wordpress/redirecionamentos.csv` (já vem dentro do tema) |
| Código-fonte do tema | `wordpress/theme-src/` + `wordpress/build_theme.py` (gera o tema a partir das páginas aprovadas em `site/`) |

## 1. Antes de começar

- WordPress 6.4 ou mais novo, PHP 8.0 ou mais novo.
- **Recomendado: instalação limpa do WordPress** (pode ser no mesmo domínio e na mesma hospedagem).
  O site atual tem os cases antigos como artigos na raiz (`/bacio-di-latte-suporte-dedicado/` etc.) e o Elementor.
  Se instalar por cima, apague esses artigos e páginas antigos — senão eles continuam no ar e os
  redirecionamentos para as páginas novas não acontecem. A página `/linkbio/` pode ser mantida.
- Faça um backup completo do site atual antes.

## 2. Plugins

- **Yoast SEO** (o site atual já usa): títulos, descrições, prévias de compartilhamento e sitemap.
- **Um plugin de SMTP** (ex.: WP Mail SMTP) para os e-mails do formulário "Solicitar proposta" chegarem
  com segurança. Configure o e-mail que recebe as propostas em Configurações › Geral.
- Não é preciso Elementor nem construtor de páginas.

## 3. Tema

Aparência › Temas › Adicionar novo › Enviar tema › `workdigital-tema.zip` › Ativar.

## 4. Conteúdo (cases, artigos, páginas e configurações)

Com acesso SSH e WP-CLI na hospedagem, a partir da pasta do WordPress:

```bash
WD_BASE=/caminho/do/repositorio WD_AUTOR=seu-login wp eval-file /caminho/do/repositorio/wordpress/importar.php
```

- `WD_AUTOR` é o login de quem assina os artigos (a bio usa esse usuário).
- Pode rodar de novo quando quiser: o que já existe é atualizado, nada é duplicado.
- O importador cria: os 16 cases (com artes, vídeos e thumbs na Biblioteca de mídia), os 22 artigos,
  as páginas Home, Soluções, Blog, Bio, Contato e Política de privacidade (como rascunho), as categorias,
  e configura o Yoast, a página inicial e a página de artigos.

Sem SSH: peça à hospedagem para rodar o comando acima (é uma vez só).

## 5. Depois da importação

1. **Configurações › Links permanentes**: estrutura personalizada `/blog/%postname%/`, base das categorias
   `blog/categoria`. Salve (isso também atualiza os endereços dos cases, `/cases/nome-do-case/`).
2. **Usuários › Seu perfil**: nome de exibição, "Informações biográficas" (texto da bio), cargo, foto,
   assinatura manuscrita (opcional), LinkedIn e Instagram. Foto e assinatura: suba a imagem na Biblioteca de mídia
   e cole o número (ID) do arquivo.
3. **Páginas › Política de privacidade**: revise o texto e publique. O aviso de cookies passa a mostrar o link.
4. **Configurações › Geral**: e-mail que recebe as propostas.
5. **Google Tag Manager**: o contêiner GTM-592RCDK9 já está no tema, com o Modo de Consentimento
   (nada de análise/anúncios antes do "Aceitar"). Nas tags do GTM, use os consentimentos
   `analytics_storage` e `ad_storage`.
6. **Search Console**: verifique o domínio e envie `https://workdigital.art.br/sitemap_index.xml`.

## 6. Como cadastrar um case novo

Cases › Adicionar case. O endereço nasce do título (ex.: "Nova Marca" → `/cases/nova-marca/`).

- **Página do case**: tipo de projeto, parágrafos 1 e 2, serviços (um por linha), link do projeto e a opção
  "Mostrar o botão Ver projeto no ar", legendas dos blocos 1, 3 e 4.
- **Artes**: as 7 imagens (bloco 5 = imagem de capa do vídeo) e os vídeos MP4/WebM do bloco 5.
  O texto alternativo de cada imagem é editado na Biblioteca de mídia.
- **Card na página de Cases**: frase, formato (grande, médio, pequeno) e os arquivos da thumb animada.
- **Destaque na home**: posição 1 a 4 na seção Works, descrição e os arquivos da thumb da home.
- **Ordem**: no quadro "Atributos" (menor número aparece primeiro). O "Próximo case" segue essa ordem.
- **Yoast**: título e descrição para o Google, no quadro do Yoast.

## 7. Como publicar um artigo

Posts › Adicionar novo: título, texto, categoria, imagem destacada (com texto alternativo) e o "Resumo"
(aparece na listagem e na home). O primeiro parágrafo pode usar a classe `lead` (bloco › Avançado › Classe CSS).
A linha fina abaixo do título fica no quadro "Linha fina" (se vazio, usa o resumo).
A home mostra sempre os 3 artigos mais recentes.

## O que o tema já faz

- Mesmo visual das páginas aprovadas (o tema é gerado a partir delas).
- SEO: Yoast + dados estruturados próprios (planos e FAQ em Soluções, CreativeWork nos cases, ProfilePage na bio).
- Redirecionamentos 301 das 64 URLs do site atual (as `/en/` vão para a home com 302 até a versão em inglês).
- Acessibilidade: "Pular para o conteúdo", foco visível, "Pausar animações", títulos em ordem.
- Imagens com versões menores automáticas (qualidade 90, originais preservadas).
- Aviso de cookies (LGPD) ligado ao Modo de Consentimento do Google.
- Formulário "Solicitar proposta" com proteção contra robôs e limite de envios.
- Página 404 com caminhos de volta.
