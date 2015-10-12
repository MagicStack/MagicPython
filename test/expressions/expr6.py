a = (a, b(a=1), {c: d(b=1), e: [a, b(z=1)]})



a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
(             : source.python
a,            : source.python
b             : meta.function-call.python, source.python
(             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
a             : meta.function-call.arguments.python, meta.function-call.python, source.python, variable.parameter.function-call.pyhton
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, source.python
1             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
,             : source.python
{             : source.python
c:            : source.python
d             : meta.function-call.python, source.python
(             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
b             : meta.function-call.arguments.python, meta.function-call.python, source.python, variable.parameter.function-call.pyhton
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, source.python
1             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
, e:          : source.python
[             : source.python
a,            : source.python
b             : meta.function-call.python, source.python
(             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
z             : meta.function-call.arguments.python, meta.function-call.python, source.python, variable.parameter.function-call.pyhton
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, source.python
1             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
]             : source.python
}             : source.python
)             : source.python
