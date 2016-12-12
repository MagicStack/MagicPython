a = rf'fo{{{2}}}'
a = rf'fo{{{bar}}}'
a = rf'fo{{2}}'





a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
rf            : source.python, storage.type.string.python, string.interpolated.python, string.regexp.quoted.single.python
'             : punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.regexp.quoted.single.python
fo            : source.python, string.interpolated.python, string.regexp.quoted.single.python
{{            : constant.character.escape.python, source.python, string.interpolated.python, string.regexp.quoted.single.python
{2}           : source.python, string.interpolated.python, string.regexp.quoted.single.python
}}            : constant.character.escape.python, source.python, string.interpolated.python, string.regexp.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.interpolated.python, string.regexp.quoted.single.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
rf            : source.python, storage.type.string.python, string.interpolated.python, string.regexp.quoted.single.python
'             : punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.regexp.quoted.single.python
fo            : source.python, string.interpolated.python, string.regexp.quoted.single.python
{{            : constant.character.escape.python, source.python, string.interpolated.python, string.regexp.quoted.single.python
{bar}         : source.python, string.interpolated.python, string.regexp.quoted.single.python
}}            : constant.character.escape.python, source.python, string.interpolated.python, string.regexp.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.interpolated.python, string.regexp.quoted.single.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
rf            : source.python, storage.type.string.python, string.interpolated.python, string.regexp.quoted.single.python
'             : punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.regexp.quoted.single.python
fo            : source.python, string.interpolated.python, string.regexp.quoted.single.python
{{2}}         : keyword.operator.quantifier.regexp, source.python, string.interpolated.python, string.regexp.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.interpolated.python, string.regexp.quoted.single.python
