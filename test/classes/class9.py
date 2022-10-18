class Foo:
    __slots__ = ()
    __match_args__ = ('key', 'name')



class         : meta.class.python, source.python, storage.type.class.python
              : meta.class.python, source.python
Foo           : entity.name.type.class.python, meta.class.python, source.python
:             : meta.class.python, punctuation.section.class.begin.python, source.python
              : source.python
__slots__     : source.python, support.variable.magic.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
(             : punctuation.parenthesis.begin.python, source.python
)             : punctuation.parenthesis.end.python, source.python
              : source.python
__match_args__ : source.python, support.variable.magic.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
(             : punctuation.parenthesis.begin.python, source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
key           : source.python, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
,             : punctuation.separator.element.python, source.python
              : source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
name          : source.python, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
)             : punctuation.parenthesis.end.python, source.python
