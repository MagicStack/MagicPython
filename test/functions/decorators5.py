@a. \
  b  .  \
   c.None.z \
    baz(q=1)
@foo.ok
def foo(): pass



@             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.definition.decorator.python, source.python
a             : entity.name.function.decorator.python, meta.function.decorator.python, source.python
.             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.separator.period.python, source.python
              : meta.function.decorator.python, source.python
\             : meta.function.decorator.python, punctuation.separator.continuation.line.python, source.python
              : meta.function.decorator.python, source.python
              : meta.function.decorator.python, source.python
b             : entity.name.function.decorator.python, meta.function.decorator.python, source.python
              : meta.function.decorator.python, source.python
.             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.separator.period.python, source.python
              : meta.function.decorator.python, source.python
\             : meta.function.decorator.python, punctuation.separator.continuation.line.python, source.python
              : meta.function.decorator.python, source.python
              : meta.function.decorator.python, source.python
c             : entity.name.function.decorator.python, meta.function.decorator.python, source.python
.             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.separator.period.python, source.python
None          : keyword.illegal.name.python, meta.function.decorator.python, source.python
.             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.separator.period.python, source.python
z             : entity.name.function.decorator.python, meta.function.decorator.python, source.python
              : meta.function.decorator.python, source.python
\             : meta.function.decorator.python, punctuation.separator.continuation.line.python, source.python
              : meta.function.decorator.python, source.python
              : meta.function.decorator.python, source.python
baz           : entity.name.function.decorator.python, meta.function.decorator.python, source.python
(             : meta.function.decorator.python, punctuation.definition.arguments.begin.python, source.python
q             : meta.function-call.arguments.python, meta.function.decorator.python, source.python, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function.decorator.python, source.python
1             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function.decorator.python, source.python
)             : meta.function.decorator.python, punctuation.definition.arguments.end.python, source.python
@             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.definition.decorator.python, source.python
foo           : entity.name.function.decorator.python, meta.function.decorator.python, source.python
.             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.separator.period.python, source.python
ok            : entity.name.function.decorator.python, meta.function.decorator.python, source.python
def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
pass          : keyword.control.flow.python, source.python
