a = r'[a-z]'
a = R'[a-z]'



a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
r             : source.python, storage.type.string.python, string.regexp.quoted.single.python
'             : punctuation.definition.string.begin.python, source.python, string.regexp.quoted.single.python
[             : constant.other.set.regexp, meta.character.set.regexp, punctuation.character.set.begin.regexp, source.python, string.regexp.quoted.single.python
a             : constant.character.set.regexp, meta.character.set.regexp, source.python, string.regexp.quoted.single.python
-             : constant.character.set.regexp, meta.character.set.regexp, source.python, string.regexp.quoted.single.python
z             : constant.character.set.regexp, meta.character.set.regexp, source.python, string.regexp.quoted.single.python
]             : constant.other.set.regexp, meta.character.set.regexp, punctuation.character.set.end.regexp, source.python, string.regexp.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.regexp.quoted.single.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
R             : source.python, storage.type.string.python, string.quoted.raw.single.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.raw.single.python
[a-z]         : source.python, string.quoted.raw.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.raw.single.python
