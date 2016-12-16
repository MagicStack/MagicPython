@foo
async def foo():
    a = 1
    async for a, b, c in b:
        async with b as d, c:
            await func(a, b=1)



@             : entity.name.function.decorator.python, meta.function.decorator.python, source.python
foo           : entity.name.function.decorator.python, meta.function.decorator.python, source.python
async         : meta.function.python, source.python, storage.type.function.async.python
              : meta.function.python, source.python
def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
1             : constant.numeric.dec.python, source.python
              : source.python
async         : keyword.control.flow.python, source.python
              : source.python
for           : keyword.control.flow.python, source.python
              : source.python
a             : source.python
,             : punctuation.separator.element.python, source.python
              : source.python
b             : source.python
,             : punctuation.separator.element.python, source.python
              : source.python
c             : source.python
              : source.python
in            : keyword.operator.logical.python, source.python
              : source.python
b             : source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
async         : keyword.control.flow.python, source.python
              : source.python
with          : keyword.control.flow.python, source.python
              : source.python
b             : source.python
              : source.python
as            : keyword.control.flow.python, source.python
              : source.python
d             : source.python
,             : punctuation.separator.element.python, source.python
              : source.python
c             : source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
await         : keyword.control.flow.python, source.python
              : source.python
func          : meta.function-call.generic.python, meta.function-call.python, source.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
a             : meta.function-call.arguments.python, meta.function-call.python, source.python
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python
b             : meta.function-call.arguments.python, meta.function-call.python, source.python, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, source.python
1             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
