class Foo(Bar, str, type=12, metaclass=FooMeta): pass



class         : meta.class.python, source.python, storage.type.class.python
              : meta.class.python, source.python
Foo           : entity.name.type.class.python, meta.class.python, source.python
(             : meta.class.inheritance.python, meta.class.python, punctuation.definition.inheritance.begin.python, source.python
Bar           : entity.other.inherited-class.python, meta.class.inheritance.python, meta.class.python, source.python
,             : meta.class.inheritance.python, meta.class.python, punctuation.separator.inheritance.python, source.python
              : meta.class.inheritance.python, meta.class.python, source.python
str           : meta.class.inheritance.python, meta.class.python, source.python, support.type.python
,             : meta.class.inheritance.python, meta.class.python, punctuation.separator.inheritance.python, source.python
              : meta.class.inheritance.python, meta.class.python, source.python
type          : entity.other.inherited-class.python, meta.class.inheritance.python, meta.class.python, source.python, variable.parameter.class.python
=             : keyword.operator.assignment.python, meta.class.inheritance.python, meta.class.python, source.python
12            : constant.numeric.dec.python, meta.class.inheritance.python, meta.class.python, source.python
,             : meta.class.inheritance.python, meta.class.python, punctuation.separator.inheritance.python, source.python
              : meta.class.inheritance.python, meta.class.python, source.python
metaclass     : meta.class.inheritance.python, meta.class.python, source.python, support.type.metaclass.python
=             : keyword.operator.assignment.python, meta.class.inheritance.python, meta.class.python, source.python
FooMeta       : entity.other.inherited-class.python, meta.class.inheritance.python, meta.class.python, source.python
)             : meta.class.inheritance.python, meta.class.python, punctuation.definition.inheritance.end.python, source.python
:             : meta.class.python, punctuation.section.class.begin.python, source.python
              : source.python
pass          : keyword.control.flow.python, source.python
