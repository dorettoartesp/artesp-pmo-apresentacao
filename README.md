# Escritório de Projetos da ARTESP — apresentação

Proposta de adoção do OpenProject como ferramenta institucional de acompanhamento de projetos da ARTESP, num escritório de projetos federado: um portfólio, cada área no seu método. Publicada no GitHub Pages como página estática, com [reveal.js](https://revealjs.com/) vendorizado — sem framework de build, sem `npm`.

**Site:** `https://dorettoartesp.github.io/artesp-pmo-apresentacao/`

## Como está organizado

| Pasta | O que é |
|---|---|
| `deck/` | **Fonte do conteúdo.** Um arquivo HTML por slide (`project/slides/<id>.html`) e o índice `project/deck.json` com a ordem. |
| `site/` | **O que o Pages serve.** `index.html` é gerado a partir de `deck/`; `css/artesp.css` é a moldura com a identidade ARTESP; `vendor/reveal/` é o reveal.js 5.1.0; `img/` tem as logos e as capturas de tela. |
| `tools/build-site.py` | Conversor `deck/` → `site/index.html`. Troca os elementos próprios do formato de origem (`x-connector`, `x-shape`, `x-icon`, `x-capture`) por SVG inline ou `<img>`. |
| `tests/` | Testes do conversor (`python3 -m unittest`). |
| `docs/superpowers/` | Design e plano da apresentação. |

## Fluxo de trabalho

```bash
make build   # deck/ -> site/index.html
make serve   # http://localhost:8080
make check   # build + guarda de texto público + testes
make shots   # um PNG por slide em output/shots/ (requer google-chrome)
```

Para alterar a apresentação, edite o slide em `deck/project/slides/` e rode `make build`. Cada slide é um `<section>` de 1920×1080 com estilos inline; `deck/project/deck.json` define a ordem.

## Capturas de tela

Cada espaço `captura: <nome>` nos slides corresponde a um arquivo `site/img/<nome>`. Coloque o arquivo lá e rode `make build`: o conversor troca o espaço pela imagem sem que o slide precise ser editado.

## Publicação

O GitHub Pages serve a branch **`gh-pages`**, que contém só o conteúdo de `site/`. Para publicar, depois de commitar em `main`:

```bash
make publish   # site/ -> branch gh-pages (git subtree) -> push
```

O repositório é público: o site é público.
