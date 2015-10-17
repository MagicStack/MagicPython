a = r'[a-z]'
a = R'[a-z]'



a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
r             : source.python, storage.type.string.python, string.regexp.quoted.python
'             : punctuation.definition.string.begin.python, source.python, string.regexp.quoted.python
[             : constant.other.set.regexp punctuation.character.set.begin.regexp, meta.character.set.regexp, source.python, string.regexp.quoted.python
a             : constant.character.set.regexp, meta.character.set.regexp, source.python, string.regexp.quoted.python
-             : constant.character.set.regexp, meta.character.set.regexp, source.python, string.regexp.quoted.python
z             : constant.character.set.regexp, meta.character.set.regexp, source.python, string.regexp.quoted.python
]             : constant.other.set.regexp punctuation.character.set.end.regexp, meta.character.set.regexp, source.python, string.regexp.quoted.python
'             : punctuation.definition.string.end.python, source.python, string.regexp.quoted.python
a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
R             : source.python, storage.type.string.python, string.quoted.raw.single.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.raw.single.python
[a-z]         : source.python, string.quoted.raw.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.raw.single.python
