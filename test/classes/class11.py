class F:
    def __init__(self, a, b=1):
        self.a = a
        self.b = b
        print(self)
        self()
        a.self = 1
        a.self.bar = 2
        self[123]



class         : meta.class.python, source.python, storage.type.class.python
              : meta.class.python, source.python
F             : entity.name.type.class.python, meta.class.python, source.python
:             : meta.class.python, punctuation.section.class.begin.python, source.python
              : meta.function.python, source.python
def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
__init__      : meta.function.python, source.python, support.function.magic.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
self          : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.python, variable.parameter.function.language.special.self.python
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
self          : source.python, variable.language.special.self.python
.             : punctuation.separator.period.python, source.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
a             : source.python
              : source.python
self          : source.python, variable.language.special.self.python
.             : punctuation.separator.period.python, source.python
b             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
b             : source.python
              : source.python
print         : meta.function-call.python, source.python, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
self          : meta.function-call.arguments.python, meta.function-call.python, source.python, variable.language.special.self.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
              : source.python
self          : meta.function-call.python, source.python, variable.language.special.self.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
              : source.python
a             : source.python
.             : punctuation.separator.period.python, source.python
self          : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
1             : constant.numeric.dec.python, source.python
              : source.python
a             : source.python
.             : punctuation.separator.period.python, source.python
self          : source.python
.             : punctuation.separator.period.python, source.python
bar           : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
2             : constant.numeric.dec.python, source.python
              : source.python
self          : meta.item-access.python, source.python, variable.language.special.self.python
[             : meta.item-access.python, punctuation.definition.arguments.begin.python, source.python
123           : constant.numeric.dec.python, meta.item-access.arguments.python, meta.item-access.python, source.python
]             : meta.item-access.python, punctuation.definition.arguments.end.python, source.python
