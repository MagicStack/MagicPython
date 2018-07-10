a = lambda `123`
# comment



a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
lambda        : meta.lambda-function.python, source.python, storage.type.function.lambda.python
              : meta.function.lambda.parameters.python, meta.lambda-function.python, source.python
`             : invalid.deprecated.backtick.python, meta.function.lambda.parameters.python, meta.lambda-function.python, source.python
123           : constant.numeric.dec.python, invalid.deprecated.backtick.python, meta.function.lambda.parameters.python, meta.lambda-function.python, source.python
`             : invalid.deprecated.backtick.python, meta.function.lambda.parameters.python, meta.lambda-function.python, source.python
              : meta.lambda-function.python, source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 comment      : comment.line.number-sign.python, source.python
