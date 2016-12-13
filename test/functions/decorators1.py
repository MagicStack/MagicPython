@some_decorator # with comment
@some.class.decorator
@some_decorator(1)
@some.decorator   (1, 3)
@some_decorator(a=2, b={'q': 42}, **kwargs)
@classmethod
def decorated(a): pass



@             : entity.name.function.decorator.python, meta.function.decorator.python, source.python
some_decorator : entity.name.function.decorator.python, meta.function.decorator.python, source.python
              : meta.function.decorator.python, source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 with comment : comment.line.number-sign.python, source.python
@             : entity.name.function.decorator.python, meta.function.decorator.python, source.python
some          : entity.name.function.decorator.python, meta.function.decorator.python, source.python
.             : entity.name.function.decorator.python, meta.function.decorator.python, source.python
class         : keyword.control.flow.python, meta.function.decorator.python, source.python
.             : entity.name.function.decorator.python, meta.function.decorator.python, source.python
decorator     : entity.name.function.decorator.python, meta.function.decorator.python, source.python
@             : entity.name.function.decorator.python, meta.function.decorator.python, source.python
some_decorator : entity.name.function.decorator.python, meta.function.decorator.python, source.python
(             : meta.function.decorator.python, punctuation.definition.arguments.begin.python, source.python
1             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function.decorator.python, source.python
)             : meta.function.decorator.python, punctuation.definition.arguments.end.python, source.python
@             : entity.name.function.decorator.python, meta.function.decorator.python, source.python
some          : entity.name.function.decorator.python, meta.function.decorator.python, source.python
.             : entity.name.function.decorator.python, meta.function.decorator.python, source.python
decorator     : entity.name.function.decorator.python, meta.function.decorator.python, source.python
              : meta.function.decorator.python, source.python
(             : meta.function.decorator.python, punctuation.definition.arguments.begin.python, source.python
1             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function.decorator.python, source.python
,             : meta.function-call.arguments.python, meta.function.decorator.python, punctuation.separator.arguments.python, source.python
              : meta.function-call.arguments.python, meta.function.decorator.python, source.python
3             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function.decorator.python, source.python
)             : meta.function.decorator.python, punctuation.definition.arguments.end.python, source.python
@             : entity.name.function.decorator.python, meta.function.decorator.python, source.python
some_decorator : entity.name.function.decorator.python, meta.function.decorator.python, source.python
(             : meta.function.decorator.python, punctuation.definition.arguments.begin.python, source.python
a             : meta.function-call.arguments.python, meta.function.decorator.python, source.python, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function.decorator.python, source.python
2             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function.decorator.python, source.python
,             : meta.function-call.arguments.python, meta.function.decorator.python, punctuation.separator.arguments.python, source.python
              : meta.function-call.arguments.python, meta.function.decorator.python, source.python
b             : meta.function-call.arguments.python, meta.function.decorator.python, source.python, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function.decorator.python, source.python
{             : meta.function-call.arguments.python, meta.function.decorator.python, punctuation.definition.dict.begin.python, source.python
'             : meta.function-call.arguments.python, meta.function.decorator.python, punctuation.definition.string.begin.python, source.python, string.quoted.single.python
q             : meta.function-call.arguments.python, meta.function.decorator.python, source.python, string.quoted.single.python
'             : meta.function-call.arguments.python, meta.function.decorator.python, punctuation.definition.string.end.python, source.python, string.quoted.single.python
:             : meta.function-call.arguments.python, meta.function.decorator.python, punctuation.separator.dict.python, source.python
              : meta.function-call.arguments.python, meta.function.decorator.python, source.python
42            : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function.decorator.python, source.python
}             : meta.function-call.arguments.python, meta.function.decorator.python, punctuation.definition.dict.end.python, source.python
,             : meta.function-call.arguments.python, meta.function.decorator.python, punctuation.separator.arguments.python, source.python
              : meta.function-call.arguments.python, meta.function.decorator.python, source.python
**            : keyword.operator.unpacking.arguments.python, meta.function-call.arguments.python, meta.function.decorator.python, source.python
kwargs        : meta.function-call.arguments.python, meta.function.decorator.python, source.python
)             : meta.function.decorator.python, punctuation.definition.arguments.end.python, source.python
@             : entity.name.function.decorator.python, meta.function.decorator.python, source.python
classmethod   : meta.function.decorator.python, source.python, support.type.python
def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
decorated     : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
a             : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
pass          : keyword.control.flow.python, source.python
