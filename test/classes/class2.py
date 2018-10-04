@dec
# Bar.name=... is not legal, but the test is for highlighter not breaking badly
class Spam(Foo.Bar, Bar.name={'very': 'odd'}):
    pass



@             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.definition.decorator.python, source.python
dec           : entity.name.function.decorator.python, meta.function.decorator.python, source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 Bar.name=... is not legal, but the test is for highlighter not breaking badly : comment.line.number-sign.python, source.python
class         : meta.class.python, source.python, storage.type.class.python
              : meta.class.python, source.python
Spam          : entity.name.type.class.python, meta.class.python, source.python
(             : meta.class.inheritance.python, meta.class.python, punctuation.definition.inheritance.begin.python, source.python
Foo           : entity.other.inherited-class.python, meta.class.inheritance.python, meta.class.python, source.python
.             : meta.class.inheritance.python, meta.class.python, punctuation.separator.period.python, source.python
Bar           : entity.other.inherited-class.python, meta.class.inheritance.python, meta.class.python, source.python
,             : meta.class.inheritance.python, meta.class.python, punctuation.separator.inheritance.python, source.python
              : meta.class.inheritance.python, meta.class.python, source.python
Bar           : entity.other.inherited-class.python, meta.class.inheritance.python, meta.class.python, source.python
.             : meta.class.inheritance.python, meta.class.python, punctuation.separator.period.python, source.python
name          : entity.other.inherited-class.python, meta.class.inheritance.python, meta.class.python, source.python
=             : keyword.operator.assignment.python, meta.class.inheritance.python, meta.class.python, source.python
{             : meta.class.inheritance.python, meta.class.python, punctuation.definition.dict.begin.python, source.python
'             : meta.class.inheritance.python, meta.class.python, punctuation.definition.string.begin.python, source.python, string.quoted.single.python
very          : meta.class.inheritance.python, meta.class.python, source.python, string.quoted.single.python
'             : meta.class.inheritance.python, meta.class.python, punctuation.definition.string.end.python, source.python, string.quoted.single.python
:             : meta.class.inheritance.python, meta.class.python, punctuation.separator.dict.python, source.python
              : meta.class.inheritance.python, meta.class.python, source.python
'             : meta.class.inheritance.python, meta.class.python, punctuation.definition.string.begin.python, source.python, string.quoted.single.python
odd           : meta.class.inheritance.python, meta.class.python, source.python, string.quoted.single.python
'             : meta.class.inheritance.python, meta.class.python, punctuation.definition.string.end.python, source.python, string.quoted.single.python
}             : meta.class.inheritance.python, meta.class.python, punctuation.definition.dict.end.python, source.python
)             : meta.class.inheritance.python, meta.class.python, punctuation.definition.inheritance.end.python, source.python
:             : meta.class.python, punctuation.section.class.begin.python, source.python
              : source.python
pass          : keyword.control.flow.python, source.python
