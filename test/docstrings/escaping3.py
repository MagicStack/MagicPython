r'''Module docstring

    (?x)                # not a regexp
        foo[20]{42}     # not a comment
'''



r             : source.python, storage.type.string.python, string.quoted.docstring.raw.multi.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.raw.multi.python
Module docstring : source.python, string.quoted.docstring.raw.multi.python
              : source.python, string.quoted.docstring.raw.multi.python
    (?x)                # not a regexp : source.python, string.quoted.docstring.raw.multi.python
        foo[20]{42}     # not a comment : source.python, string.quoted.docstring.raw.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.docstring.raw.multi.python
