a = rf'{{foo}}'
a = r'\{foo\}'




a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
rf            : source.python, storage.type.string.python, string.interpolated.python, string.regexp.quoted.single.python
'             : punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.regexp.quoted.single.python
{{            : constant.character.escape.python, source.python, string.interpolated.python, string.regexp.quoted.single.python
foo           : source.python, string.interpolated.python, string.regexp.quoted.single.python
}}            : constant.character.escape.python, source.python, string.interpolated.python, string.regexp.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.interpolated.python, string.regexp.quoted.single.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
r             : source.python, storage.type.string.python, string.regexp.quoted.single.python
'             : punctuation.definition.string.begin.python, source.python, string.regexp.quoted.single.python
\{            : constant.character.escape.regexp, source.python, string.regexp.quoted.single.python
foo           : source.python, string.regexp.quoted.single.python
\}            : constant.character.escape.regexp, source.python, string.regexp.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.regexp.quoted.single.python
