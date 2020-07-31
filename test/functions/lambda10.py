showcase = lambda a, /, b, *, c: (a + b + c)




showcase      : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
lambda        : meta.lambda-function.python, source.python, storage.type.function.lambda.python
              : meta.function.lambda.parameters.python, meta.lambda-function.python, source.python
a             : meta.function.lambda.parameters.python, meta.lambda-function.python, source.python, variable.parameter.function.language.python
,             : meta.function.lambda.parameters.python, meta.lambda-function.python, punctuation.separator.parameters.python, source.python
              : meta.function.lambda.parameters.python, meta.lambda-function.python, source.python
/             : keyword.operator.positional.parameter.python, meta.function.lambda.parameters.python, meta.lambda-function.python, source.python
,             : meta.function.lambda.parameters.python, meta.lambda-function.python, source.python
b             : meta.function.lambda.parameters.python, meta.lambda-function.python, source.python, variable.parameter.function.language.python
,             : meta.function.lambda.parameters.python, meta.lambda-function.python, punctuation.separator.parameters.python, source.python
              : meta.function.lambda.parameters.python, meta.lambda-function.python, source.python
*             : keyword.operator.unpacking.parameter.python, meta.function.lambda.parameters.python, meta.lambda-function.python, source.python
,             : meta.function.lambda.parameters.python, meta.lambda-function.python, source.python
c             : meta.function.lambda.parameters.python, meta.lambda-function.python, source.python, variable.parameter.function.language.python
:             : meta.lambda-function.python, punctuation.section.function.lambda.begin.python, source.python
              : source.python
(             : punctuation.parenthesis.begin.python, source.python
a             : source.python
              : source.python
+             : keyword.operator.arithmetic.python, source.python
              : source.python
b             : source.python
              : source.python
+             : keyword.operator.arithmetic.python, source.python
              : source.python
c             : source.python
)             : punctuation.parenthesis.end.python, source.python
