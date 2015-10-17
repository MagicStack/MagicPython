a = r'foo[^]'
a = r'foo[]'


a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
r             : source.python, storage.type.string.python, string.regexp.quoted.python
'             : punctuation.definition.string.begin.python, source.python, string.regexp.quoted.python
foo           : source.python, string.regexp.quoted.python
[^]           : source.python, string.regexp.quoted.python
'             : punctuation.definition.string.end.python, source.python, string.regexp.quoted.python
a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
r             : source.python, storage.type.string.python, string.regexp.quoted.python
'             : punctuation.definition.string.begin.python, source.python, string.regexp.quoted.python
foo           : source.python, string.regexp.quoted.python
[]            : source.python, string.regexp.quoted.python
'             : punctuation.definition.string.end.python, source.python, string.regexp.quoted.python
