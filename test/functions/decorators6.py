@a.   b  .  \
   c.None.z(foo=BAR). \
       baz[1:2]
@foo.class.bar[]
@foo.ok '''
def foo(): pass


@             : entity.name.function.decorator.python, meta.function.decorator.python, source.python
a             : entity.name.function.decorator.python, meta.function.decorator.python, source.python
.             : entity.name.function.decorator.python, meta.function.decorator.python, source.python
              : meta.function.decorator.python, source.python
b             : entity.name.function.decorator.python, meta.function.decorator.python, source.python
              : meta.function.decorator.python, source.python
.             : entity.name.function.decorator.python, meta.function.decorator.python, source.python
              : meta.function.decorator.python, source.python
\             : meta.function.decorator.python, punctuation.separator.continuation.line.python, source.python
              : meta.function.decorator.python, source.python
              : meta.function.decorator.python, source.python
c             : entity.name.function.decorator.python, meta.function.decorator.python, source.python
.             : entity.name.function.decorator.python, meta.function.decorator.python, source.python
None          : keyword.illegal.name.python, meta.function.decorator.python, source.python
.             : entity.name.function.decorator.python, meta.function.decorator.python, source.python
z             : entity.name.function.decorator.python, meta.function.decorator.python, source.python
(             : meta.function.decorator.python, punctuation.definition.arguments.begin.python, source.python
foo           : meta.function-call.arguments.python, meta.function.decorator.python, source.python, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function.decorator.python, source.python
BAR           : constant.other.caps.python, meta.function-call.arguments.python, meta.function.decorator.python, source.python
)             : meta.function.decorator.python, punctuation.definition.arguments.end.python, source.python
. \           : invalid.illegal.decorator.python, meta.function.decorator.python, source.python
              : source.python
baz           : meta.item-access.python, source.python
[             : meta.item-access.python, punctuation.definition.arguments.begin.python, source.python
1             : constant.numeric.dec.python, meta.item-access.arguments.python, meta.item-access.python, source.python
:             : meta.item-access.arguments.python, meta.item-access.python, punctuation.separator.slice.python, source.python
2             : constant.numeric.dec.python, meta.item-access.arguments.python, meta.item-access.python, source.python
]             : meta.item-access.python, punctuation.definition.arguments.end.python, source.python
@             : entity.name.function.decorator.python, meta.function.decorator.python, source.python
foo           : entity.name.function.decorator.python, meta.function.decorator.python, source.python
.             : entity.name.function.decorator.python, meta.function.decorator.python, source.python
class         : keyword.control.flow.python, meta.function.decorator.python, source.python
.             : entity.name.function.decorator.python, meta.function.decorator.python, source.python
bar           : entity.name.function.decorator.python, meta.function.decorator.python, source.python
[]            : invalid.illegal.decorator.python, meta.function.decorator.python, source.python
@             : entity.name.function.decorator.python, meta.function.decorator.python, source.python
foo           : entity.name.function.decorator.python, meta.function.decorator.python, source.python
.             : entity.name.function.decorator.python, meta.function.decorator.python, source.python
ok            : entity.name.function.decorator.python, meta.function.decorator.python, source.python
              : invalid.illegal.decorator.python, meta.function.decorator.python, source.python
'''           : invalid.illegal.decorator.python, meta.function.decorator.python, source.python
def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
pass          : keyword.control.flow.python, source.python
