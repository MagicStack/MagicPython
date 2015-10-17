a = "normal {{ normal }} normal {10!r} normal {fo.__add__!s}".format(fo=1)



a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.double.single.python
normal        : source.python, string.quoted.double.single.python
{{            : constant.character.format.python, source.python, string.quoted.double.single.python
 normal       : source.python, string.quoted.double.single.python
}}            : constant.character.format.python, source.python, string.quoted.double.single.python
 normal       : source.python, string.quoted.double.single.python
{10           : constant.character.format.python, source.python, string.quoted.double.single.python
!r            : constant.character.format.python, source.python, storage.type.format.python, string.quoted.double.single.python
}             : constant.character.format.python, source.python, string.quoted.double.single.python
 normal       : source.python, string.quoted.double.single.python
{fo.__add__   : constant.character.format.python, source.python, string.quoted.double.single.python
!s            : constant.character.format.python, source.python, storage.type.format.python, string.quoted.double.single.python
}             : constant.character.format.python, source.python, string.quoted.double.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.double.single.python
.             : source.python
format        : meta.function-call.python, source.python
(             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
fo            : meta.function-call.arguments.python, meta.function-call.python, source.python, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, source.python
1             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
