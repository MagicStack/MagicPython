.PHONY: all test release

all:
	npm install syntaxdev

test: release
	./node_modules/.bin/syntaxdev test --tests test/**/*.py --syntax MagicPython.YAML-tmLanguage

release:
	./node_modules/.bin/syntaxdev build-plist --in MagicPython.YAML-tmLanguage --out MagicPython.tmLanguage
	./node_modules/.bin/syntaxdev build-cson --in MagicPython.YAML-tmLanguage --out atom/MagicPython.cson
