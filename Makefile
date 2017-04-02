PY?=python
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=/home/vorakl/repos/my/github/vorakl.github.io
CONFFILE=$(BASEDIR)/sitedev.py
PUBLISHCONF=$(BASEDIR)/siteprod.py
STATICDIR=$(BASEDIR)/theme/static

GITHUB_PAGES_BRANCH=master

PORT ?= 80
DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif

.PHONY: html help serve publish gh

help:
	@echo 'Makefile for a pelican Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make html                           (re)generate the web site          '
	@echo '   make publish                        generate using production settings '
	@echo '   make serve [PORT=80]                serve site at http://localhost:80  '
	@echo '   make github                         upload the web site via gh-pages   '
	@echo '                                                                          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo '                                                                          '

html:   
	@$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

bundle:
	@cd $(STATICDIR) && \
	cat bootstrap.min.css bootstrap.min.responsive.css local.min.css pygments.min.css > bootstrap-pygments.bundle.min.css && \
	cat jquery.min.js bootstrap-collapse.min.js > jquery-bootstrap-collapse.bundle.min.js


serve:
	@echo 'Launching a docker container with Nginx on port $(PORT)'
	@docker run --rm -it -p $(PORT):80 -v $(OUTPUTDIR):/usr/share/nginx/html nginx:mainline-alpine

publish: 
	@$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

gh: publish
	@cd $(OUTPUTDIR) && \
	  git add . && \
	  git commit -m "New content" && \
	  git push origin $(GITHUB_PAGES_BRANCH)
