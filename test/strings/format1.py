a = "{0[ ]:X>+10d}"
a = "{0[ ]!s:X>+10d}"
a = "{0[ ]:Xd>+10d}" #invalid



a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
{0[ ]         : constant.character.format.placeholder.other.python, meta.format.brace.python, source.python, string.quoted.single.python
:X>+10d       : constant.character.format.placeholder.other.python, meta.format.brace.python, source.python, storage.type.format.python, string.quoted.single.python
}             : constant.character.format.placeholder.other.python, meta.format.brace.python, source.python, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
{0[ ]         : constant.character.format.placeholder.other.python, meta.format.brace.python, source.python, string.quoted.single.python
!s            : constant.character.format.placeholder.other.python, meta.format.brace.python, source.python, storage.type.format.python, string.quoted.single.python
:X>+10d       : constant.character.format.placeholder.other.python, meta.format.brace.python, source.python, storage.type.format.python, string.quoted.single.python
}             : constant.character.format.placeholder.other.python, meta.format.brace.python, source.python, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
{0[ ]         : constant.character.format.placeholder.other.python, meta.format.brace.python, source.python, string.quoted.single.python
:             : constant.character.format.placeholder.other.python, meta.format.brace.python, source.python, storage.type.format.python, string.quoted.single.python
Xd>+10d}      : constant.character.format.placeholder.other.python, meta.format.brace.python, source.python, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
              : source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
invalid       : comment.line.number-sign.python, source.python
