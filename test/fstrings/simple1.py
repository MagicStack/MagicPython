a = f"{0[ ]:X>+10d}"
a = f"{0[ ]!s:X>+10d}"
a = f"{0[ ]:Xd>+10d}" #invalid




a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
f             : meta.fstring.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.quoted.single.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
0             : constant.numeric.dec.python, meta.fstring.python, source.python
[             : meta.fstring.python, punctuation.definition.list.begin.python, source.python
              : meta.fstring.python, source.python
]             : meta.fstring.python, punctuation.definition.list.end.python, source.python
:X>+10d       : meta.fstring.python, source.python, storage.type.format.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
"             : meta.fstring.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.single.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
f             : meta.fstring.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.quoted.single.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
0             : constant.numeric.dec.python, meta.fstring.python, source.python
[             : meta.fstring.python, punctuation.definition.list.begin.python, source.python
              : meta.fstring.python, source.python
]             : meta.fstring.python, punctuation.definition.list.end.python, source.python
!s            : meta.fstring.python, source.python, storage.type.format.python
:X>+10d       : meta.fstring.python, source.python, storage.type.format.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
"             : meta.fstring.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.single.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
f             : meta.fstring.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.quoted.single.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
0             : constant.numeric.dec.python, meta.fstring.python, source.python
[             : meta.fstring.python, punctuation.definition.list.begin.python, source.python
              : meta.fstring.python, source.python
]             : meta.fstring.python, punctuation.definition.list.end.python, source.python
:             : meta.fstring.python, punctuation.separator.colon.python, source.python
Xd            : meta.fstring.python, source.python
>             : keyword.operator.comparison.python, meta.fstring.python, source.python
+             : keyword.operator.arithmetic.python, meta.fstring.python, source.python
10d           : invalid.illegal.name.python, meta.fstring.python, source.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
"             : meta.fstring.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.single.python
              : source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
invalid       : comment.line.number-sign.python, source.python
