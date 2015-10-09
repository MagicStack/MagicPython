anon = lambda -> qqq[None]: None
def f(): return 1 # this line should not break



anon          : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
lambda        : meta.lambda-function.python, source.python, storage.type.function.lambda.python
              : meta.function.lambda.parameters.python, meta.lambda-function.python, source.python
->            : invalid.illegal.annotation.python, meta.function.lambda.parameters.python, meta.lambda-function.python, source.python
 qqq[None]    : meta.function.lambda.parameters.python, meta.lambda-function.python, source.python
:             : meta.lambda-function.python, punctuation.section.function.lambda.begin.python, source.python
              : source.python
None          : constant.language.python, source.python
def           : source.python, storage.type.function.python
              : source.python
f             : meta.function-call.python, source.python
(             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
:             : source.python
return        : keyword.control.flow.python, source.python
              : source.python
1             : constant.numeric.dec.python, source.python
              : source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 this line should not break : comment.line.number-sign.python, source.python
