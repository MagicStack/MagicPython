->
def f(): pass
$
?
a=$('.class').fuuuu(baz=1)
# we recover just fine
b = !some_ruby?
# hey ;)



->            : invalid.illegal.annotation.python, source.python
def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
f             : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
pass          : keyword.control.flow.python, source.python
$             : invalid.illegal.operator.python, source.python
?             : invalid.illegal.operator.python, source.python
a             : source.python
=             : keyword.operator.assignment.python, source.python
$             : invalid.illegal.operator.python, source.python
(             : punctuation.parenthesis.begin.python, source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
.class        : source.python, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
)             : punctuation.parenthesis.end.python, source.python
.             : punctuation.separator.period.python, source.python
fuuuu         : meta.function-call.generic.python, meta.function-call.python, source.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
baz           : meta.function-call.arguments.python, meta.function-call.python, source.python, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, source.python
1             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 we recover just fine : comment.line.number-sign.python, source.python
b             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
!             : invalid.illegal.operator.python, source.python
some_ruby     : source.python
?             : invalid.illegal.operator.python, source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 hey ;)       : comment.line.number-sign.python, source.python
