.PHONY: all test

all:
	npm install syntaxtest

test:
	./node_modules/.bin/syntaxtest --tests test/**/*.py --syntax MagicPython.YAML-tmLanguage
