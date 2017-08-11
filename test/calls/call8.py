foo. __class__(foo=bar)
foo. __class__ (foo=bar)
foo. __add__ (foo=bar)
foo. __add__(foo=bar)



foo           : source.python
.             : punctuation.separator.period.python, source.python
              : source.python
__class__     : meta.function-call.python, source.python, support.variable.magic.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
foo           : meta.function-call.arguments.python, meta.function-call.python, source.python, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, source.python
bar           : meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
foo           : source.python
.             : punctuation.separator.period.python, source.python
              : source.python
__class__     : meta.function-call.python, source.python, support.variable.magic.python
              : meta.function-call.python, source.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
foo           : meta.function-call.arguments.python, meta.function-call.python, source.python, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, source.python
bar           : meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
foo           : source.python
.             : punctuation.separator.period.python, source.python
              : source.python
__add__       : meta.function-call.python, source.python, support.function.magic.python
              : meta.function-call.python, source.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
foo           : meta.function-call.arguments.python, meta.function-call.python, source.python, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, source.python
bar           : meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
foo           : source.python
.             : punctuation.separator.period.python, source.python
              : source.python
__add__       : meta.function-call.python, source.python, support.function.magic.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
foo           : meta.function-call.arguments.python, meta.function-call.python, source.python, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, source.python
bar           : meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
