a = "{(([ ]:X>+10d}"
a = "{(([ ]!s:X>+10d}"
a = "{(([ ]:Xd>+10d}" #invalid



a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.double.single.python
{(([ ]        : constant.character.format.python, source.python, string.quoted.double.single.python
:X>+10d       : constant.character.format.python, source.python, string.quoted.double.single.python, support.other.format.python
}             : constant.character.format.python, source.python, string.quoted.double.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.double.single.python
a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.double.single.python
{(([ ]        : constant.character.format.python, source.python, string.quoted.double.single.python
!s            : constant.character.format.python, source.python, storage.type.format.python, string.quoted.double.single.python
:X>+10d       : constant.character.format.python, source.python, string.quoted.double.single.python, support.other.format.python
}             : constant.character.format.python, source.python, string.quoted.double.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.double.single.python
a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.double.single.python
{(([ ]        : constant.character.format.python, source.python, string.quoted.double.single.python
:             : constant.character.format.python, source.python, string.quoted.double.single.python, support.other.format.python
Xd>+10d       : constant.character.format.python, source.python, string.quoted.double.single.python
}             : constant.character.format.python, source.python, string.quoted.double.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.double.single.python
              : source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
invalid       : comment.line.number-sign.python, source.python
