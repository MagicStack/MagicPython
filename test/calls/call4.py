foo.1
foo(bar=baz)(ham=sam)
foo.None and foo.None.baz



foo           : source.python
.             : punctuation.separator.period.python, source.python
1             : source.python
foo           : meta.function-call.generic.python, meta.function-call.python, source.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
bar           : meta.function-call.arguments.python, meta.function-call.python, source.python, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, source.python
baz           : meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.arguments.end.python, source.python
(             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
ham           : meta.function-call.arguments.python, meta.function-call.python, source.python, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, source.python
sam           : meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
foo           : source.python
.             : punctuation.separator.period.python, source.python
None          : keyword.illegal.name.python, source.python
              : source.python
and           : keyword.operator.logical.python, source.python
              : source.python
foo           : source.python
.             : punctuation.separator.period.python, source.python
None          : keyword.illegal.name.python, source.python
.             : punctuation.separator.period.python, source.python
baz           : source.python
