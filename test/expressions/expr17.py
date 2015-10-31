a++
b--
++a
--b
a++c
c--b
a(--a)



a             : source.python
++            : invalid.illegal.operator.python, source.python
b             : source.python
--            : invalid.illegal.operator.python, source.python
++            : invalid.illegal.operator.python, source.python
a             : source.python
--            : invalid.illegal.operator.python, source.python
b             : source.python
a             : source.python
++            : invalid.illegal.operator.python, source.python
c             : source.python
c             : source.python
--            : invalid.illegal.operator.python, source.python
b             : source.python
a             : meta.function-call.generic.python, meta.function-call.python, source.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
--            : invalid.illegal.operator.python, meta.function-call.arguments.python, meta.function-call.python, source.python
a             : meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
