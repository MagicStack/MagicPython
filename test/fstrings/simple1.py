a = f"{0[ ]:X>+10d}"
a = f"{0[ ]!s:X>+10d}"
a = f"{0[ ]:Xd>+10d}" #invalid




a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
f             : source.python, storage.type.string.python, string.quoted.single.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
{             : constant.character.format.placeholder.other.python, source.python
0             : constant.numeric.dec.python, source.python
[             : punctuation.definition.list.begin.python, source.python
              : source.python
]             : punctuation.definition.list.end.python, source.python
:X>+10d       : source.python, support.other.format.python
}             : constant.character.format.placeholder.other.python, source.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
f             : source.python, storage.type.string.python, string.quoted.single.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
{             : constant.character.format.placeholder.other.python, source.python
0             : constant.numeric.dec.python, source.python
[             : punctuation.definition.list.begin.python, source.python
              : source.python
]             : punctuation.definition.list.end.python, source.python
!s            : source.python, storage.type.format.python
:X>+10d       : source.python, support.other.format.python
}             : constant.character.format.placeholder.other.python, source.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
f             : source.python, storage.type.string.python, string.quoted.single.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
{             : constant.character.format.placeholder.other.python, source.python
0             : constant.numeric.dec.python, source.python
[             : punctuation.definition.list.begin.python, source.python
              : source.python
]             : punctuation.definition.list.end.python, source.python
:Xd           : source.python, support.other.format.python
>             : keyword.operator.comparison.python, source.python
+             : keyword.operator.arithmetic.python, source.python
10d           : invalid.illegal.name.python, source.python
}             : constant.character.format.placeholder.other.python, source.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
              : source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
invalid       : comment.line.number-sign.python, source.python
