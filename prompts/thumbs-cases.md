# Prompt: thumbs dos projetos da página de Cases (Work Digital)

Você vai produzir as thumbs dos projetos da página de Cases do site da Work Digital. Os arquivos que você gerar serão encaixados no site sem nenhuma edição, então siga as especificações abaixo à risca.

## Como a thumb funciona no site

- **Parada:** a thumb mostra uma imagem estática (o "poster").
- **Mouse em cima:**
  - começa a tocar um vídeo curto em loop, no mesmo enquadramento do poster;
  - a imagem dá um zoom leve, de cerca de 4%, feito pelo próprio site;
  - aparece o círculo "Ver case".
- **Mouse sai:** o vídeo pausa e volta ao poster.
- **Celular:** não existe "mouse em cima", então aparece só o poster.
- **Modo lista:** ao passar o mouse no nome do projeto, uma prévia flutuante de 4:3 mostra o mesmo vídeo.

Por isso, cada projeto precisa de **2 arquivos**: um poster (imagem) e um vídeo curto em loop. Não mande GIF: GIF fica pesado e com cores ruins. Também não mande elementos separados (camadas): a animação já deve vir pronta no vídeo.

Se algum projeto não tiver animação, mande só o poster. O site mostra a imagem parada com o zoom no hover.

## Tamanhos

Cada projeto ocupa um dos três formatos da grade. Produza no formato indicado para o projeto:

| Formato | Proporção | Poster | Vídeo |
|---|---|---|---|
| Grande (largura total) | 16:7,5 | 2400 × 1125 px | 1600 × 750 px |
| Médio (meia largura) | 4:3 | 1600 × 1200 px | 1200 × 900 px |
| Pequeno (um terço) | 4:5 | 1200 × 1500 px | 960 × 1200 px |

**Área de segurança:** no celular, todas as thumbs são cortadas para 4:3,4. No modo lista, a prévia é 4:3. Por isso, mantenha logo, título e elementos importantes no **centro da imagem, ocupando no máximo cerca de 60% da largura e 70% da altura**. As bordas podem ser cortadas.

## Poster (imagem estática)

- Formato **WebP** (qualidade 80–85). Se não for possível, use JPG com qualidade 80.
- Peso ideal: até 300 KB (grande) ou 200 KB (médio e pequeno).
- Deve ser **idêntico ao primeiro quadro do vídeo**, para não haver salto quando a animação começa.
- Sem cantos arredondados nem bordas: o site já arredonda os cantos (16px).

## Vídeo (animação no hover)

- Formato **MP4 (H.264)**. Se possível, mande também uma versão **WebM (VP9)**.
- Duração de **4 a 8 segundos**, com **loop perfeito**: o último quadro emenda no primeiro.
- **Sem áudio** (remova a trilha).
- 30 fps.
- Peso: até 2,5 MB (grande) ou 1,5 MB (médio e pequeno).
- Animação suave, por exemplo:
  - telas do site rolando dentro do mockup;
  - leve movimento de câmera;
  - elementos entrando aos poucos.
- Evite cortes bruscos e piscadas.
- O primeiro quadro deve ser exatamente o poster.

## Estilo visual

- Mockups em fundo coerente com o site da Work:
  - tons escuros, de grafite #121316 a roxo #24123E;
  - ou as cores do próprio cliente.
- Pode usar a paleta da Work nos detalhes:
  - roxo #6025E1;
  - lilás #CBB6FF;
  - verde #04CD8F;
  - vinho #C00252.
- Não coloque nas thumbs texto que o site já mostra (nome do cliente, descrição, serviços). O site escreve esses textos abaixo da imagem.

## Nomes dos arquivos

Use o "slug" do projeto: minúsculas, sem acento, com hífen.

- `vice-versa.webp` (poster)
- `vice-versa.mp4` (vídeo)
- `vice-versa.webm` (vídeo, opcional)

## Dados de cada projeto (mandar junto, numa lista)

Para cada projeto, informe:

1. Slug (ex.: `vice-versa`)
2. Nome do cliente (ex.: Vice Versa Estamparia)
3. Frase curta do projeto (ex.: Rebranding e site para uma estamparia de 40 anos)
4. Serviços (até 3, ex.: Branding, Website)
5. Formato na grade: grande, médio ou pequeno
6. Ordem em que deve aparecer na página
7. Link do site no ar (para o botão "Ver projeto no ar" da página interna)

## Resumo do que entregar por projeto

- 1 poster WebP, no tamanho do formato escolhido, com o conteúdo importante no centro.
- 1 vídeo MP4 sem áudio, de 4 a 8 segundos, em loop perfeito, começando no mesmo quadro do poster (WebM opcional).
- Os dados do projeto (os 7 itens acima).
