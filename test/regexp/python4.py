a = r"""
    (?x)
        foo
"""
a = br"""
    (?x)
        foo
"""
a = rb"""
    (?x)
        foo
"""
a = Br"""
    (?x)
        foo
"""
a = rB"""
    (?x)
        foo
"""



a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
r             : source.python, storage.type.string.python, string.regexp.quoted.multi.python
"""           : punctuation.definition.string.begin.python, source.python, string.regexp.quoted.multi.python
              : source.python, string.regexp.quoted.multi.python
(?x)          : source.python, storage.modifier.flag.regexp, string.regexp.quoted.multi.python
        foo   : source.python, string.regexp.quoted.multi.python
"""           : punctuation.definition.string.end.python, source.python, string.regexp.quoted.multi.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
br            : source.python, storage.type.string.python, string.regexp.quoted.multi.python
"""           : punctuation.definition.string.begin.python, source.python, string.regexp.quoted.multi.python
              : source.python, string.regexp.quoted.multi.python
(?x)          : source.python, storage.modifier.flag.regexp, string.regexp.quoted.multi.python
        foo   : source.python, string.regexp.quoted.multi.python
"""           : punctuation.definition.string.end.python, source.python, string.regexp.quoted.multi.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
rb            : source.python, storage.type.string.python, string.regexp.quoted.multi.python
"""           : punctuation.definition.string.begin.python, source.python, string.regexp.quoted.multi.python
              : source.python, string.regexp.quoted.multi.python
(?x)          : source.python, storage.modifier.flag.regexp, string.regexp.quoted.multi.python
        foo   : source.python, string.regexp.quoted.multi.python
"""           : punctuation.definition.string.end.python, source.python, string.regexp.quoted.multi.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
Br            : source.python, storage.type.string.python, string.regexp.quoted.multi.python
"""           : punctuation.definition.string.begin.python, source.python, string.regexp.quoted.multi.python
              : source.python, string.regexp.quoted.multi.python
(?x)          : source.python, storage.modifier.flag.regexp, string.regexp.quoted.multi.python
        foo   : source.python, string.regexp.quoted.multi.python
"""           : punctuation.definition.string.end.python, source.python, string.regexp.quoted.multi.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
rB            : source.python, storage.type.string.python, string.regexp.quoted.multi.python
"""           : punctuation.definition.string.begin.python, source.python, string.regexp.quoted.multi.python
              : source.python, string.regexp.quoted.multi.python
(?x)          : source.python, storage.modifier.flag.regexp, string.regexp.quoted.multi.python
        foo   : source.python, string.regexp.quoted.multi.python
"""           : punctuation.definition.string.end.python, source.python, string.regexp.quoted.multi.python
