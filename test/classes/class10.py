class Foo(Bar(q=1) (w=2) (e=3)): pass



class         : meta.class.python, source.python, storage.type.class.python
              : meta.class.python, source.python
Foo           : entity.name.type.class.python, meta.class.python, source.python
(             : meta.class.inheritance.python, meta.class.python, punctuation.definition.inheritance.begin.python, source.python
Bar           : entity.other.inherited-class.python, meta.class.inheritance.python, meta.class.python, meta.function-call.python, source.python
(             : meta.class.inheritance.python, meta.class.python, meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
q             : meta.class.inheritance.python, meta.class.python, meta.function-call.arguments.python, meta.function-call.python, source.python, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.class.inheritance.python, meta.class.python, meta.function-call.arguments.python, meta.function-call.python, source.python
1             : constant.numeric.dec.python, meta.class.inheritance.python, meta.class.python, meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.class.inheritance.python, meta.class.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.arguments.end.python, source.python
              : meta.class.inheritance.python, meta.class.python, meta.function-call.arguments.python, meta.function-call.python, source.python
(             : meta.class.inheritance.python, meta.class.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
w             : meta.class.inheritance.python, meta.class.python, meta.function-call.arguments.python, meta.function-call.python, source.python, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.class.inheritance.python, meta.class.python, meta.function-call.arguments.python, meta.function-call.python, source.python
2             : constant.numeric.dec.python, meta.class.inheritance.python, meta.class.python, meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.class.inheritance.python, meta.class.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.arguments.end.python, source.python
              : meta.class.inheritance.python, meta.class.python, meta.function-call.arguments.python, meta.function-call.python, source.python
(             : meta.class.inheritance.python, meta.class.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
e             : meta.class.inheritance.python, meta.class.python, meta.function-call.arguments.python, meta.function-call.python, source.python, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.class.inheritance.python, meta.class.python, meta.function-call.arguments.python, meta.function-call.python, source.python
3             : constant.numeric.dec.python, meta.class.inheritance.python, meta.class.python, meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.class.inheritance.python, meta.class.python, meta.function-call.python, punctuation.definition.arguments.end.python, source.python
)             : meta.class.inheritance.python, meta.class.python, punctuation.definition.inheritance.end.python, source.python
:             : meta.class.python, punctuation.section.class.begin.python, source.python
              : source.python
pass          : keyword.control.flow.python, source.python
