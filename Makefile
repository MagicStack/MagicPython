.PHONY: all test release

all: devenv release

test: release
#	Run tests
	./node_modules/.bin/syntaxdev test --tests test/**/*.py --syntax grammars/MagicPython.syntax.yaml
	./node_modules/.bin/syntaxdev test --tests test/**/*.re --syntax grammars/MagicRegExp.syntax.yaml

# 	Check if the version specified in "package.json" matches the latest git tag
	@if [ \
		`cat package.json | grep -e '^[[:space:]]*"version":' | sed -e 's/[[:space:]]*"version":[[:space:]]*"\(.*\)",/\1/'` \
		!= \
		`git describe --tags --abbrev=0 | sed -e 's/v\([[:digit:]]\{1,\}\.[[:digit:]]\{1,\}\.[[:digit:]]\{1,\}\).*/\1/'` \
	] ; \
		then echo "Error: package.version != git.tag" && exit 1 ; fi

devenv:
	npm install syntaxdev@0.0.9

release:
	./node_modules/.bin/syntaxdev build-plist --in grammars/MagicPython.syntax.yaml --out grammars/MagicPython.tmLanguage
	./node_modules/.bin/syntaxdev build-plist --in grammars/MagicRegExp.syntax.yaml --out grammars/MagicRegExp.tmLanguage

	./node_modules/.bin/syntaxdev build-cson --in grammars/MagicPython.syntax.yaml --out grammars/MagicPython.cson
	./node_modules/.bin/syntaxdev build-cson --in grammars/MagicRegExp.syntax.yaml --out grammars/MagicRegExp.cson

	./node_modules/.bin/syntaxdev scopes --syntax grammars/MagicPython.syntax.yaml > misc/scopes
