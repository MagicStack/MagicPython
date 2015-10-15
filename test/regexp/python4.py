r"""
    (?x)
        foo
"""
br"""
    (?x)
        foo
"""
rb"""
    (?x)
        foo
"""
Br"""
    (?x)
        foo
"""
rB"""
    (?x)
        foo
"""



r             : source.python, storage.type.string.python, string.regexp.quoted.triple.python
"""           : punctuation.definition.string.begin.python, source.python, string.regexp.quoted.triple.python
              : source.python, string.regexp.quoted.triple.python
(?x)          : source.python, storage.modifier.flag.regexp, string.regexp.quoted.triple.python
        foo   : source.python, string.regexp.quoted.triple.python
"""           : punctuation.definition.string.end.python, source.python, string.regexp.quoted.triple.python
br            : source.python, storage.type.string.python, string.regexp.quoted.triple.python
"""           : punctuation.definition.string.begin.python, source.python, string.regexp.quoted.triple.python
              : source.python, string.regexp.quoted.triple.python
(?x)          : source.python, storage.modifier.flag.regexp, string.regexp.quoted.triple.python
        foo   : source.python, string.regexp.quoted.triple.python
"""           : punctuation.definition.string.end.python, source.python, string.regexp.quoted.triple.python
rb            : source.python, storage.type.string.python, string.regexp.quoted.triple.python
"""           : punctuation.definition.string.begin.python, source.python, string.regexp.quoted.triple.python
              : source.python, string.regexp.quoted.triple.python
(?x)          : source.python, storage.modifier.flag.regexp, string.regexp.quoted.triple.python
        foo   : source.python, string.regexp.quoted.triple.python
"""           : punctuation.definition.string.end.python, source.python, string.regexp.quoted.triple.python
Br            : source.python, storage.type.string.python, string.regexp.quoted.triple.python
"""           : punctuation.definition.string.begin.python, source.python, string.regexp.quoted.triple.python
              : source.python, string.regexp.quoted.triple.python
(?x)          : source.python, storage.modifier.flag.regexp, string.regexp.quoted.triple.python
        foo   : source.python, string.regexp.quoted.triple.python
"""           : punctuation.definition.string.end.python, source.python, string.regexp.quoted.triple.python
rB            : source.python, storage.type.string.python, string.regexp.quoted.triple.python
"""           : punctuation.definition.string.begin.python, source.python, string.regexp.quoted.triple.python
              : source.python, string.regexp.quoted.triple.python
(?x)          : source.python, storage.modifier.flag.regexp, string.regexp.quoted.triple.python
        foo   : source.python, string.regexp.quoted.triple.python
"""           : punctuation.definition.string.end.python, source.python, string.regexp.quoted.triple.python
