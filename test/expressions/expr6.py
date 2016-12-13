a = (a, b(a=1), {c: d(b=1), e: [a, b(z=1)]})



a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
(             : punctuation.parenthesis.begin.python, source.python
a             : source.python
,             : punctuation.separator.element.python, source.python
              : source.python
b             : meta.function-call.generic.python, meta.function-call.python, source.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
a             : meta.function-call.arguments.python, meta.function-call.python, source.python, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, source.python
1             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
,             : punctuation.separator.element.python, source.python
              : source.python
{             : punctuation.definition.dict.begin.python, source.python
c             : source.python
:             : punctuation.separator.dict.python, source.python
              : source.python
d             : meta.function-call.generic.python, meta.function-call.python, source.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
b             : meta.function-call.arguments.python, meta.function-call.python, source.python, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, source.python
1             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
,             : punctuation.separator.element.python, source.python
              : source.python
e             : source.python
:             : punctuation.separator.dict.python, source.python
              : source.python
[             : punctuation.definition.list.begin.python, source.python
a             : source.python
,             : punctuation.separator.element.python, source.python
              : source.python
b             : meta.function-call.generic.python, meta.function-call.python, source.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
z             : meta.function-call.arguments.python, meta.function-call.python, source.python, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, source.python
1             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
]             : punctuation.definition.list.end.python, source.python
}             : punctuation.definition.dict.end.python, source.python
)             : punctuation.parenthesis.end.python, source.python
