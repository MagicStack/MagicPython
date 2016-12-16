anon = lambda a,
              d=1: None
def foo(): pass



anon          : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
lambda        : meta.lambda-function.python, source.python, storage.type.function.lambda.python
              : meta.function.lambda.parameters.python, meta.lambda-function.python, source.python
a             : meta.function.lambda.parameters.python, meta.lambda-function.python, source.python, variable.parameter.function.language.python
,             : meta.function.lambda.parameters.python, meta.lambda-function.python, punctuation.separator.parameters.python, source.python
              : meta.lambda-function.python, source.python
               : source.python
d             : source.python
=             : keyword.operator.assignment.python, source.python
1             : constant.numeric.dec.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
None          : constant.language.python, source.python
def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
pass          : keyword.control.flow.python, source.python
