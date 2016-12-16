cdef foo(): pass



cdef          : source.python
              : source.python
foo           : meta.function-call.generic.python, meta.function-call.python, source.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
pass          : keyword.control.flow.python, source.python
