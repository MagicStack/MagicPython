foo.class(a)
foo.and()
foo.if



foo           : source.python
.             : punctuation.separator.period.python, source.python
class         : keyword.control.flow.python, meta.function-call.python, source.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
a             : meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
foo           : source.python
.             : punctuation.separator.period.python, source.python
and           : keyword.control.flow.python, meta.function-call.python, source.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
foo           : source.python
.             : punctuation.separator.period.python, source.python
if            : keyword.control.flow.python, source.python
