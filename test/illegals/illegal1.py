->
def f(): pass
$
?
a=$('.class').fuuuu(baz=1)
# we recover just fine
b = !some_ruby?
# hey ;)



->            : invalid.illegal.annotation.python, source.python
def           : source.python, storage.type.function.python
              : source.python
f             : meta.function-call.python, source.python
(             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
:             : source.python
pass          : keyword.control.flow.python, source.python
$             : invalid.illegal.character.python, source.python
?             : invalid.illegal.character.python, source.python
a             : source.python
=             : keyword.operator.assignment.python, source.python
$             : invalid.illegal.character.python, source.python
(             : source.python
'             : source.python, string.quoted.single.python
.class        : source.python, string.quoted.single.python
'             : source.python, string.quoted.single.python
)             : source.python
.             : source.python
fuuuu         : meta.function-call.python, source.python
(             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
baz           : meta.function-call.arguments.python, meta.function-call.python, source.python, variable.parameter.function-call.pyhton
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, source.python
1             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 we recover just fine : comment.line.number-sign.python, source.python
b             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
!             : invalid.illegal.character.python, source.python
some_ruby     : source.python
?             : invalid.illegal.character.python, source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 hey ;)       : comment.line.number-sign.python, source.python
