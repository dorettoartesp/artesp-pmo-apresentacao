.DEFAULT_GOAL := help
.PHONY: help build check serve shots status publish

CHROME ?= google-chrome
SITE   := site
SHOTS  := output/shots

help: ## Lista os comandos
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-8s\033[0m %s\n", $$1, $$2}'

build: ## Gera site/index.html a partir de deck/ (fonte do conteúdo)
	python3 tools/build-site.py deck $(SITE)/index.html

check: build ## Falha se o site contiver texto que não pode ir ao público
	@! grep -inE 'enterprise|objetivo 04|plano estrat|token|desbloque' $(SITE)/index.html \
	  || { echo "texto proibido em $(SITE)/index.html"; exit 1; }
	@python3 -m unittest tests.test_build_site
	@echo "ok"

serve: ## Serve o site localmente em http://localhost:8080
	cd $(SITE) && python3 -m http.server 8080

shots: ## Renderiza todos os slides em PNG (output/shots/) para conferência
	@mkdir -p $(SHOTS)
	@n=$$(grep -c '<section data-transition' $(SITE)/index.html); i=0; \
	while [ $$i -lt $$n ]; do \
	  $(CHROME) --headless=new --disable-gpu --hide-scrollbars --no-sandbox --window-size=1920,1080 \
	    --virtual-time-budget=6000 --screenshot=$(SHOTS)/$$(printf '%02d' $$i).png \
	    "file://$(CURDIR)/$(SITE)/index.html#/$$i" >/dev/null 2>&1; i=$$((i+1)); done; \
	echo "$$n slides em $(SHOTS)/"

publish: ## Publica site/ na branch gh-pages (origem do GitHub Pages)
	git subtree split --prefix site -b gh-pages
	git push -f origin gh-pages
	git branch -D gh-pages
	@echo "Publicado: https://dorettoartesp.github.io/artesp-pmo-apresentacao/ (o build do Pages leva cerca de um minuto)"

status: ## git status
	@git status --short
