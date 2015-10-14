.PHONY: all test release

all:
	npm install syntaxdev@0.0.4

test: release
#	Run tests
	./node_modules/.bin/syntaxdev test --tests test/**/*.py --syntax grammars/MagicPython.YAML-tmLanguage

# 	Check if the version specified in "package.json" matches the latest git tag
	@[[ `cat package.json | grep '^[[:space:]]*"version":' | sed -e 's/[[:space:]]*"version":[[:space:]]*"\(.*\)",/\1/'` = `git describe --tags | sed -e 's/v\([[:digit:]]\{1,\}\.[[:digit:]]\{1,\}\.[[:digit:]]\{1,\}\).*/\1/'` ]] || (echo "Error: package.version != git.tag" && exit 1)

release:
	./node_modules/.bin/syntaxdev build-plist --in grammars/MagicPython.YAML-tmLanguage --out grammars/MagicPython.tmLanguage
	./node_modules/.bin/syntaxdev build-cson --in grammars/MagicPython.YAML-tmLanguage --out grammars/MagicPython.cson
