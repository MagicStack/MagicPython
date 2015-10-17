class Spam(Foo, from=12):
    pass



class         : meta.class.python, source.python, storage.type.class.python
              : meta.class.python, source.python
Spam          : entity.name.type.class.python, meta.class.python, source.python
(             : meta.class.inheritance.python, meta.class.python, punctuation.definition.inheritance.begin.python, source.python
Foo           : entity.other.inherited-class.python, meta.class.inheritance.python, meta.class.python, source.python
,             : meta.class.inheritance.python, meta.class.python, punctuation.separator.inheritance.python, source.python
              : meta.class.inheritance.python, meta.class.python, source.python
from          : keyword.control.flow.python, meta.class.inheritance.python, meta.class.python, source.python
=             : keyword.operator.assignment.python, meta.class.inheritance.python, meta.class.python, source.python
12            : constant.numeric.dec.python, meta.class.inheritance.python, meta.class.python, source.python
)             : meta.class.inheritance.python, meta.class.python, punctuation.definition.inheritance.end.python, source.python
:             : meta.class.python, punctuation.section.class.begin.python, source.python
              : source.python
pass          : keyword.control.flow.python, source.python
