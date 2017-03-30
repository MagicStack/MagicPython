a = f'''hello { foo("bar")/23 !r:f} times'''




a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
f             : meta.fstring.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.multi.python
'''           : meta.fstring.python, punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.quoted.multi.python
hello         : meta.fstring.python, source.python, string.interpolated.python, string.quoted.multi.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
              : meta.fstring.python, source.python
foo           : meta.fstring.python, meta.function-call.generic.python, meta.function-call.python, source.python
(             : meta.fstring.python, meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
"             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.python, string.quoted.single.python
bar           : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python, string.quoted.single.python
"             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.python, string.quoted.single.python
)             : meta.fstring.python, meta.function-call.python, punctuation.definition.arguments.end.python, source.python
/             : keyword.operator.arithmetic.python, meta.fstring.python, source.python
23            : constant.numeric.dec.python, meta.fstring.python, source.python
              : meta.fstring.python, source.python
!r            : meta.fstring.python, source.python, storage.type.format.python
:f            : meta.fstring.python, source.python, storage.type.format.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
 times        : meta.fstring.python, source.python, string.interpolated.python, string.quoted.multi.python
'''           : meta.fstring.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.multi.python
