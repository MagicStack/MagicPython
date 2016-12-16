if isinstance(t1, TypeVar): # type: ignore
    continue



if            : keyword.control.flow.python, source.python
              : source.python
isinstance    : meta.function-call.python, source.python, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
t1            : meta.function-call.arguments.python, meta.function-call.python, source.python
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python
TypeVar       : meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
#             : comment.line.number-sign.python, meta.typehint.comment.python, source.python
type:         : comment.line.number-sign.python, comment.typehint.directive.notation.python, meta.typehint.comment.python, source.python
              : comment.line.number-sign.python, meta.typehint.comment.python, source.python
ignore        : comment.line.number-sign.python, comment.typehint.ignore.notation.python, meta.typehint.comment.python, source.python
              : source.python
continue      : keyword.control.flow.python, source.python
