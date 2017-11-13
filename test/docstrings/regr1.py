#:
    @asd
    def foo():
        pass



#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
:             : comment.line.number-sign.python, source.python
              : meta.function.decorator.python, source.python
@             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.definition.decorator.python, source.python
asd           : entity.name.function.decorator.python, meta.function.decorator.python, source.python
              : meta.function.python, source.python
def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
pass          : keyword.control.flow.python, source.python
