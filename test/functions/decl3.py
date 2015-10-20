# testing annotations split over multiple lines
def __init__(self, a:('abc' 'def')=123, boo: 'abc'

                         'def' = foo(n(m=0), baz=
                            13)) -> 123 : 123



#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 testing annotations split over multiple lines : comment.line.number-sign.python, source.python
def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
__init__      : meta.function.python, source.python, support.function.magic.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
self          : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.python, variable.parameter.function.language.special.self.python
,             : meta.function.parameters.python, meta.function.python, punctuation.separator.parameters.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
a             : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.python
:             : meta.function.parameters.python, meta.function.python, punctuation.separator.annotation.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.parenthesis.begin.python, source.python
'             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.begin.python, source.python, string.quoted.single.python
abc           : meta.function.parameters.python, meta.function.python, source.python, string.quoted.single.python
'             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.end.python, source.python, string.quoted.single.python
              : meta.function.parameters.python, meta.function.python, source.python
'             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.begin.python, source.python, string.quoted.single.python
def           : meta.function.parameters.python, meta.function.python, source.python, string.quoted.single.python
'             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.end.python, source.python, string.quoted.single.python
)             : meta.function.parameters.python, meta.function.python, punctuation.parenthesis.end.python, source.python
=             : keyword.operator.assignment.python, meta.function.parameters.python, meta.function.python, source.python
123           : constant.numeric.dec.python, meta.function.parameters.python, meta.function.python, source.python
,             : meta.function.parameters.python, meta.function.python, punctuation.separator.parameters.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
boo           : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.python
:             : meta.function.parameters.python, meta.function.python, punctuation.separator.annotation.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
'             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.begin.python, source.python, string.quoted.single.python
abc           : meta.function.parameters.python, meta.function.python, source.python, string.quoted.single.python
'             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.end.python, source.python, string.quoted.single.python
              : meta.function.parameters.python, meta.function.python, source.python
                          : meta.function.parameters.python, meta.function.python, source.python
'             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.begin.python, source.python, string.quoted.single.python
def           : meta.function.parameters.python, meta.function.python, source.python, string.quoted.single.python
'             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.end.python, source.python, string.quoted.single.python
              : meta.function.parameters.python, meta.function.python, source.python
=             : keyword.operator.assignment.python, meta.function.parameters.python, meta.function.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
foo           : meta.function-call.generic.python, meta.function-call.python, meta.function.parameters.python, meta.function.python, source.python
(             : meta.function-call.python, meta.function.parameters.python, meta.function.python, punctuation.definition.arguments.begin.python, source.python
n             : meta.function-call.arguments.python, meta.function-call.generic.python, meta.function-call.python, meta.function.parameters.python, meta.function.python, source.python
(             : meta.function-call.arguments.python, meta.function-call.python, meta.function.parameters.python, meta.function.python, punctuation.definition.arguments.begin.python, source.python
m             : meta.function-call.arguments.python, meta.function-call.python, meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, meta.function.parameters.python, meta.function.python, source.python
0             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, meta.function.parameters.python, meta.function.python, source.python
)             : meta.function-call.arguments.python, meta.function-call.python, meta.function.parameters.python, meta.function.python, punctuation.definition.arguments.end.python, source.python
,             : meta.function-call.arguments.python, meta.function-call.python, meta.function.parameters.python, meta.function.python, punctuation.separator.arguments.python, source.python
              : meta.function-call.arguments.python, meta.function-call.python, meta.function.parameters.python, meta.function.python, source.python
baz           : meta.function-call.arguments.python, meta.function-call.python, meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, meta.function.parameters.python, meta.function.python, source.python
                             : meta.function-call.arguments.python, meta.function-call.python, meta.function.parameters.python, meta.function.python, source.python
13            : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, meta.function.parameters.python, meta.function.python, source.python
)             : meta.function-call.python, meta.function.parameters.python, meta.function.python, punctuation.definition.arguments.end.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
              : meta.function.python, source.python
->            : meta.function.python, punctuation.separator.annotation.result.python, source.python
              : meta.function.python, source.python
123           : constant.numeric.dec.python, meta.function.python, source.python
              : meta.function.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
123           : constant.numeric.dec.python, source.python
