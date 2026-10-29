# Para continuar de outro computador

Cole o texto abaixo como primeira mensagem ao Claude Code, aberto na raiz deste
repositório. Ele descreve o estado do trabalho e o que falta.

---

Estou continuando o deck `artesp-pmo-apresentacao` em outra máquina. Leia o
`README.md` e este arquivo antes de agir.

**Estado.** Os 12 slides estão prontos e publicados em
`https://dorettoartesp.github.io/artesp-pmo-apresentacao/` (branch
`gh-pages`, gerada por `make publish`). O texto está em registro formal e
técnico; mantenha esse registro em qualquer alteração. O design e o plano da
apresentação não ficam neste repositório, que é público: estão no repositório
privado `artesp-pmo`, em `docs/superpowers/`. Não traga documentos de trabalho,
nomes de pessoas nem detalhes de configuração interna para cá.

**O que falta.**

1. Capturas de tela, em `site/img/`, com estes nomes exatos:
   `scrum-sutid.png` (quadro Scrum de um projeto da SUTID),
   `gantt-surod.png` (Gantt de um projeto da SUROD) e
   `portfolio.png` (lista de projetos do Portfólio ARTESP). O conversor troca
   os espaços reservados pelas imagens sozinho. Proporções: 800×450 nas duas
   primeiras, 880×458 na terceira (a imagem é recortada por `object-fit:cover`
   a partir do canto superior esquerdo; capture a tela cheia). Depois de
   colocar as imagens: tirar o trecho "· capturas a atualizar" do rodapé de
   `deck/project/slides/lado-a-lado.html`.
2. Fluxo para publicar: `make check` (build + guarda de texto público +
   testes), conferir com `make shots` e ler os PNGs em `output/shots/`,
   `git commit`, `make publish`. O `publish` recusa `site/` não commitado.
3. Melhorias pequenas apontadas em revisão, ainda não feitas; faça só se eu
   pedir: rodapé do slide 9 ("OpenProject · software livre, GPL v3" em vez
   de "Community Edition"); `box-shadow:none` no bloco reservado em
   `tools/build-site.py`; `tests/__init__.py` para `python3 -m unittest`
   descobrir os testes; "somente na intranet" no rodapé de `no-ar.html`;
   retirar o numeral "01" de `decisao.html`; ícone `Link` em vez de `Check`
   no cartão "Grupos do AD" de `transparencia.html`; título do slide 4 menos
   parecido com o da capa.

**Regras deste repositório.** Um HTML por slide em `deck/project/slides/`,
ordem em `deck/project/deck.json`, moldura copiada do `artesp-estrategia`.
Commits em português, com `Co-Authored-By` do Claude. Antes de qualquer
`make publish`, `make check` tem de passar.
