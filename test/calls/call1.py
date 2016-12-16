some_call(A, b, c[1], *args, FOO=lambda:{'q': 42}, **kwargs)



some_call     : meta.function-call.generic.python, meta.function-call.python, source.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
A             : meta.function-call.arguments.python, meta.function-call.python, source.python
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python
b             : meta.function-call.arguments.python, meta.function-call.python, source.python
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python
c             : meta.function-call.arguments.python, meta.function-call.python, meta.item-access.python, source.python
[             : meta.function-call.arguments.python, meta.function-call.python, meta.item-access.python, punctuation.definition.arguments.begin.python, source.python
1             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, meta.item-access.arguments.python, meta.item-access.python, source.python
]             : meta.function-call.arguments.python, meta.function-call.python, meta.item-access.python, punctuation.definition.arguments.end.python, source.python
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python
*             : keyword.operator.unpacking.arguments.python, meta.function-call.arguments.python, meta.function-call.python, source.python
args          : meta.function-call.arguments.python, meta.function-call.python, source.python
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python
FOO           : meta.function-call.arguments.python, meta.function-call.python, source.python, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, source.python
lambda        : meta.function-call.arguments.python, meta.function-call.python, meta.lambda-function.python, source.python, storage.type.function.lambda.python
:             : meta.function-call.arguments.python, meta.function-call.python, meta.lambda-function.python, punctuation.section.function.lambda.begin.python, source.python
{             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.dict.begin.python, source.python
'             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.python, string.quoted.single.python
q             : meta.function-call.arguments.python, meta.function-call.python, source.python, string.quoted.single.python
'             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.python, string.quoted.single.python
:             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.dict.python, source.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python
42            : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, source.python
}             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.dict.end.python, source.python
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python
**            : keyword.operator.unpacking.arguments.python, meta.function-call.arguments.python, meta.function-call.python, source.python
kwargs        : meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
