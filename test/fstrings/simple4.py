a = f'''hello { foo("bar")/23 !r:f} times'''




a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
f             : source.python, storage.type.string.python, string.quoted.multi.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.multi.python
hello         : source.python, string.quoted.multi.python
{             : constant.character.format.placeholder.other.python, source.python
              : source.python
foo           : meta.function-call.generic.python, meta.function-call.python, source.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.python, string.quoted.single.python
bar           : meta.function-call.arguments.python, meta.function-call.python, source.python, string.quoted.single.python
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.python, string.quoted.single.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
/             : keyword.operator.arithmetic.python, source.python
23            : constant.numeric.dec.python, source.python
              : source.python
!r            : source.python, storage.type.format.python
:f            : source.python, support.other.format.python
}             : constant.character.format.placeholder.other.python, source.python
 times        : source.python, string.quoted.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.multi.python
