def foo()
    -> notOK:
    pass



def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
              : source.python
->            : invalid.illegal.annotation.python, source.python
              : source.python
notOK         : source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
pass          : keyword.control.flow.python, source.python
