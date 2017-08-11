class F:
    @classmethod
    def meth(cls, a, b=1):
        cls.a = a
        cls.b = b
        print(cls)
        cls()
        cls + 1
        a.cls = 1
        a.cls.__name__
        cls[123]



class         : meta.class.python, source.python, storage.type.class.python
              : meta.class.python, source.python
F             : entity.name.type.class.python, meta.class.python, source.python
:             : meta.class.python, punctuation.section.class.begin.python, source.python
              : meta.function.decorator.python, source.python
@             : entity.name.function.decorator.python, meta.function.decorator.python, source.python
classmethod   : meta.function.decorator.python, source.python, support.type.python
              : meta.function.python, source.python
def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
meth          : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
cls           : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.python, variable.parameter.function.language.special.cls.python
,             : meta.function.parameters.python, meta.function.python, punctuation.separator.parameters.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
a             : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.python
,             : meta.function.parameters.python, meta.function.python, punctuation.separator.parameters.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
b             : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.python
=             : keyword.operator.python, meta.function.parameters.python, meta.function.python, source.python
1             : constant.numeric.dec.python, meta.function.parameters.python, meta.function.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
cls           : source.python, variable.language.special.cls.python
.             : punctuation.separator.period.python, source.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
a             : source.python
              : source.python
cls           : source.python, variable.language.special.cls.python
.             : punctuation.separator.period.python, source.python
b             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
b             : source.python
              : source.python
print         : meta.function-call.python, source.python, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
cls           : meta.function-call.arguments.python, meta.function-call.python, source.python, variable.language.special.cls.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
              : source.python
cls           : meta.function-call.python, source.python, variable.language.special.cls.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
              : source.python
cls           : source.python, variable.language.special.cls.python
              : source.python
+             : keyword.operator.arithmetic.python, source.python
              : source.python
1             : constant.numeric.dec.python, source.python
              : source.python
a             : source.python
.             : punctuation.separator.period.python, source.python
cls           : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
1             : constant.numeric.dec.python, source.python
              : source.python
a             : source.python
.             : punctuation.separator.period.python, source.python
cls           : source.python
.             : punctuation.separator.period.python, source.python
__name__      : source.python, support.variable.magic.python
              : source.python
cls           : meta.item-access.python, source.python, variable.language.special.cls.python
[             : meta.item-access.python, punctuation.definition.arguments.begin.python, source.python
123           : constant.numeric.dec.python, meta.item-access.arguments.python, meta.item-access.python, source.python
]             : meta.item-access.python, punctuation.definition.arguments.end.python, source.python
