id = Field[uuid.UUID] (
    uuid.UUID,
    inheritable=False,
    simpledelta=False,
    allow_ddl_set=True,
)





id            : source.python, support.function.builtin.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
Field         : meta.indexed-name.python, meta.item-access.python, source.python
[             : meta.item-access.python, punctuation.definition.arguments.begin.python, source.python
uuid          : meta.item-access.arguments.python, meta.item-access.python, source.python
.             : meta.item-access.arguments.python, meta.item-access.python, meta.member.access.python, punctuation.separator.period.python, source.python
UUID          : constant.other.caps.python, meta.item-access.arguments.python, meta.item-access.python, meta.member.access.python, source.python
]             : meta.item-access.python, punctuation.definition.arguments.end.python, source.python
              : source.python
(             : punctuation.definition.arguments.begin.python, source.python
              : meta.function-call.arguments.python, source.python
uuid          : meta.function-call.arguments.python, source.python
.             : meta.function-call.arguments.python, meta.member.access.python, punctuation.separator.period.python, source.python
UUID          : constant.other.caps.python, meta.function-call.arguments.python, meta.member.access.python, source.python
,             : meta.function-call.arguments.python, punctuation.separator.arguments.python, source.python
              : meta.function-call.arguments.python, source.python
inheritable   : meta.function-call.arguments.python, source.python, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, source.python
False         : constant.language.python, meta.function-call.arguments.python, source.python
,             : meta.function-call.arguments.python, punctuation.separator.arguments.python, source.python
              : meta.function-call.arguments.python, source.python
simpledelta   : meta.function-call.arguments.python, source.python, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, source.python
False         : constant.language.python, meta.function-call.arguments.python, source.python
,             : meta.function-call.arguments.python, punctuation.separator.arguments.python, source.python
              : meta.function-call.arguments.python, source.python
allow_ddl_set : meta.function-call.arguments.python, source.python, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, source.python
True          : constant.language.python, meta.function-call.arguments.python, source.python
,             : meta.function-call.arguments.python, punctuation.separator.arguments.python, source.python
)             : punctuation.definition.arguments.end.python, source.python
