''' foo bar XXX baz '''

def foo():
    ''' foo FIXME baz '''



'''           : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.multi.python
 foo bar      : source.python, string.quoted.docstring.multi.python
XXX           : keyword.codetag.notation.python, source.python, string.quoted.docstring.multi.python
 baz          : source.python, string.quoted.docstring.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.docstring.multi.python
              : source.python
def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.multi.python
 foo          : source.python, string.quoted.docstring.multi.python
FIXME         : keyword.codetag.notation.python, source.python, string.quoted.docstring.multi.python
 baz          : source.python, string.quoted.docstring.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.docstring.multi.python
