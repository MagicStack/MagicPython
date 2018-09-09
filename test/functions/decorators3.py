@ f . bar (baz = 1)
def foo(): pass



@             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.definition.decorator.python, source.python
              : meta.function.decorator.python, source.python
f             : entity.name.function.decorator.python, meta.function.decorator.python, source.python
              : meta.function.decorator.python, source.python
.             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.separator.period.python, source.python
              : meta.function.decorator.python, source.python
bar           : entity.name.function.decorator.python, meta.function.decorator.python, source.python
              : meta.function.decorator.python, source.python
(             : meta.function.decorator.python, punctuation.definition.arguments.begin.python, source.python
baz           : meta.function-call.arguments.python, meta.function.decorator.python, source.python, variable.parameter.function-call.python
              : meta.function-call.arguments.python, meta.function.decorator.python, source.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function.decorator.python, source.python
              : meta.function-call.arguments.python, meta.function.decorator.python, source.python
1             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function.decorator.python, source.python
)             : meta.function.decorator.python, punctuation.definition.arguments.end.python, source.python
def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
pass          : keyword.control.flow.python, source.python
