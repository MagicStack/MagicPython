.PHONY: all ci-test test release devenv publish release_sublime

all: devenv release

ci-test: release
#	Run tests
	./node_modules/.bin/syntaxdev test --tests test/**/*.py --syntax grammars/src/MagicPython.syntax.yaml
	./node_modules/.bin/syntaxdev test --tests test/**/*.re --syntax grammars/src/MagicRegExp.syntax.yaml

# 	Check if the version specified in "package.json" matches the latest git tag
	@if [ \
		`cat package.json | grep -e '^[[:space:]]*"version":' | sed -e 's/[[:space:]]*"version":[[:space:]]*"\(.*\)",/\1/'` \
		!= \
		`git describe --tags --abbrev=0 | sed -e 's/v\([[:digit:]]\{1,\}\.[[:digit:]]\{1,\}\.[[:digit:]]\{1,\}\).*/\1/'` \
	] ; \
		then echo "Error: package.version != git.tag" && exit 1 ; fi

test: ci-test
	atom -t .

devenv:
	npm install syntaxdev@0.0.16

release:
	./node_modules/.bin/syntaxdev build-plist --in grammars/src/MagicPython.syntax.yaml --out grammars/MagicPython.tmLanguage
	./node_modules/.bin/syntaxdev build-plist --in grammars/src/MagicRegExp.syntax.yaml --out grammars/MagicRegExp.tmLanguage

	./node_modules/.bin/syntaxdev build-cson --in grammars/src/MagicPython.syntax.yaml --out grammars/MagicPython.cson
	./node_modules/.bin/syntaxdev build-cson --in grammars/src/MagicRegExp.syntax.yaml --out grammars/MagicRegExp.cson

	./node_modules/.bin/syntaxdev scopes --syntax grammars/src/MagicPython.syntax.yaml > misc/scopes

	./node_modules/.bin/syntaxdev atom-spec --package-name MagicPython --tests test/**/*.py --syntax grammars/src/MagicPython.syntax.yaml --out test/atom-spec/python-spec.js
	./node_modules/.bin/syntaxdev atom-spec --package-name MagicPython --tests test/**/*.re --syntax grammars/src/MagicRegExp.syntax.yaml --out test/atom-spec/python-re-spec.js

release_sublime:
	./node_modules/.bin/syntaxdev build-plist --in grammars/src/MagicPython.syntax.yaml --out grammars/MagicPython.tmLanguage
	./node_modules/.bin/syntaxdev build-plist --in grammars/src/MagicRegExp.syntax.yaml --out grammars/MagicRegExp.tmLanguage

	rm -f grammars/*.sublime-syntax
	sed -i.bak '/<!-- AUTOGENERATED FROM .*/g' grammars/MagicPython.tmLanguage
	sed -i.bak '/<?xml version="1.0".*/g' grammars/MagicPython.tmLanguage
	sed -i.bak '/<!DOCTYPE plist PUBLIC */g' grammars/MagicPython.tmLanguage

	sed -i.bak '/<!-- AUTOGENERATED FROM .*/g' grammars/MagicRegExp.tmLanguage
	sed -i.bak '/<?xml version="1.0".*/g' grammars/MagicRegExp.tmLanguage
	sed -i.bak '/<!DOCTYPE plist PUBLIC */g' grammars/MagicRegExp.tmLanguage
	subl -w grammars/MagicPython.tmLanguage --command convert_syntax --command save
	subl -w grammars/MagicRegExp.tmLanguage --command convert_syntax --command save
	rm -f grammars/*.tmLanguage.bak
	git checkout grammars/MagicPython.tmLanguage
	git checkout grammars/MagicRegExp.tmLanguage

publish: test
	apm publish patch
	rm -rf ./node_modules/syntaxdev
	vsce publish
