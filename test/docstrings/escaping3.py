r'''Module docstring

    (?x)                # not a regexp
        foo[20]{42}     # not a comment
'''



r             : source.python, storage.type.string.python, string.quoted.docstring.raw.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.raw.python
Module docstring : source.python, string.quoted.docstring.raw.python
              : source.python, string.quoted.docstring.raw.python
    (?x)                # not a regexp : source.python, string.quoted.docstring.raw.python
        foo[20]{42}     # not a comment : source.python, string.quoted.docstring.raw.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.docstring.raw.python
