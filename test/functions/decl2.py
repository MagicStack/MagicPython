def result_annot(lambda, lambda=) -> qqq[None]:
    pass


def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
result_annot  : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
lambda        : meta.function.parameters.python, meta.function.python, source.python, storage.type.function.lambda.python
,             : meta.function.parameters.python, meta.function.python, source.python
lambda        : keyword.control.flow.python, meta.function.parameters.python, meta.function.python, source.python
=             : keyword.operator.python, meta.function.parameters.python, meta.function.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
              : meta.function.python, source.python
->            : meta.function.python, punctuation.separator.annotation.result.python, source.python
              : meta.function.python, source.python
qqq           : meta.function.python, meta.item-access.python, source.python
[             : meta.function.python, meta.item-access.python, punctuation.definition.arguments.begin.python, source.python
None          : constant.language.python, meta.function.python, meta.item-access.arguments.python, meta.item-access.python, source.python
]             : meta.function.python, meta.item-access.python, punctuation.definition.arguments.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
pass          : keyword.control.flow.python, source.python
