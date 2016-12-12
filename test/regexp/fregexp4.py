a = rf'fo{{2}}'
a = r'fo{{2}}'
a = r'fo{2}'





a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
rf            : source.python, storage.type.string.python, string.interpolated.python, string.regexp.quoted.single.python
'             : punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.regexp.quoted.single.python
fo            : source.python, string.interpolated.python, string.regexp.quoted.single.python
{{2}}         : keyword.operator.quantifier.regexp, source.python, string.interpolated.python, string.regexp.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.interpolated.python, string.regexp.quoted.single.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
r             : source.python, storage.type.string.python, string.regexp.quoted.single.python
'             : punctuation.definition.string.begin.python, source.python, string.regexp.quoted.single.python
fo{           : source.python, string.regexp.quoted.single.python
{2}           : keyword.operator.quantifier.regexp, source.python, string.regexp.quoted.single.python
}             : source.python, string.regexp.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.regexp.quoted.single.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
r             : source.python, storage.type.string.python, string.regexp.quoted.single.python
'             : punctuation.definition.string.begin.python, source.python, string.regexp.quoted.single.python
fo            : source.python, string.regexp.quoted.single.python
{2}           : keyword.operator.quantifier.regexp, source.python, string.regexp.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.regexp.quoted.single.python
