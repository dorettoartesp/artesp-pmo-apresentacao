# Para continuar de outro computador

Cole o texto abaixo como primeira mensagem ao Claude Code, aberto na raiz deste
repositório. Ele descreve o estado do trabalho e o que falta.

---

Estou continuando o deck `artesp-pmo-apresentacao` em outra máquina. Leia o
`README.md` e este arquivo antes de agir.

**Estado.** Os 13 slides estão prontos e publicados em
`https://dorettoartesp.github.io/artesp-pmo-apresentacao/` (branch
`gh-pages`, gerada por `make publish`). O texto está em registro formal e
técnico; mantenha esse registro em qualquer alteração. O design e o plano da
apresentação não ficam neste repositório, que é público: estão no repositório
privado `artesp-pmo`, em `docs/superpowers/`. Não traga documentos de trabalho,
nomes de pessoas nem detalhes de configuração interna para cá.

**O que falta.**

1. Nada bloqueia a publicação: as quatro capturas estão em `site/img/` (`backlog-sutid.png` é a do slide 6, Scrum, projeto `exemplo-scrum-contratos`)
   (feitas em 29/10/2026 na homologação, com os projetos de exemplo da
   release `f134b98`), o slide 4 mostra os sete modelos e o site foi
   publicado. Para refazer uma captura: tela cheia 1920×1080, menu lateral
   recolhido, colunas "Objetivo estratégico" e "Patrocinador" ocultas na
   lista de projetos; recortar a partir do canto superior esquerdo em
   16:9 (as duas primeiras) ou 880:458 (a terceira); `make build`.
2. Fluxo para publicar: `make check` (build + guarda de texto público +
   testes), conferir com `make shots` e ler os PNGs em `output/shots/`,
   `git commit`, `make publish`. O `publish` recusa `site/` não commitado.
3. Portfólios por superintendência: feitos no `artesp-pmo` (release
   `55b346e`; correções da revisão de hom na release `8e3576f`, em hom
   desde 29/10/2026: colunas nas vistas, quadros por sprint só com status
   do baseline, burndown em degraus). Capturas refeitas nesse estado
   (`portfolio.png`, `scrum-sutid.png`, `backlog-sutid.png`). O burndown
   ainda extrapola a altura da tela; o roteiro não o mostra. Projetos de
   teste criados à mão em hom (`teste`, `teste2`) foram ocultados por JS
   antes da captura.
   Para a lista do portfólio: `/projects` com filtros ativo = sim e
   projeto modelo = não, painel de filtros fechado, menu lateral
   recolhido, colunas Favorito, Público, Criado em, Armazenamento,
   Objetivo estratégico e Patrocinador ocultas.
4. Slide 3 traz o recorte do organograma (`site/img/organograma-superintendencias.png`,
   gerado de `organograma.jpeg` com `crop=1310:335:500:632`); a SUTID é
   superintendência funcional. O organograma é a fonte dos nomes
   (decisão de 29/10/2026). Release `3a97632` do `artesp-pmo`
   (em hom desde 29/10/2026) troca SUINV por SUPEP e "Superintendência
   Rodoviária" por "Superintendência de Rodovias"; `portfolio.png` refeita
   nesse estado. dev ainda tem `portfolio-suinv` (handoff
   `deploy-record-3a97632.md`). Slide 13: cartões e itens 1 a 4 do roteiro
   abrem páginas de hom em nova aba.
5. Produção está na release `13202f2` (um modelo só); os sete modelos estão
   só em homologação. Promover antes da apresentação ou demonstrar em hom.

**Regras deste repositório.** Um HTML por slide em `deck/project/slides/`,
ordem em `deck/project/deck.json`, moldura copiada do `artesp-estrategia`.
Commits em português, com `Co-Authored-By` do Claude. Antes de qualquer
`make publish`, `make check` tem de passar.
