a = r"foo#not a comment"
a = r"""
    (?x)        # multi-line regexp
        foo     # comment
"""
a = R"""
    (?x)        # not a
        foo     # comment
"""



a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
r             : source.python, storage.type.string.python, string.regexp.quoted.python
"             : punctuation.definition.string.begin.python, source.python, string.regexp.quoted.python
foo#not a comment : source.python, string.regexp.quoted.python
"             : punctuation.definition.string.end.python, source.python, string.regexp.quoted.python
a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
r             : source.python, storage.type.string.python, string.regexp.quoted.triple.python
"""           : punctuation.definition.string.begin.python, source.python, string.regexp.quoted.triple.python
              : source.python, string.regexp.quoted.triple.python
(?x)          : source.python, storage.modifier.flag.regexp, string.regexp.quoted.triple.python
              : source.python, string.regexp.quoted.triple.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python, string.regexp.quoted.triple.python
 multi-line regexp : comment.line.number-sign.python, source.python, string.regexp.quoted.triple.python
        foo      : source.python, string.regexp.quoted.triple.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python, string.regexp.quoted.triple.python
 comment      : comment.line.number-sign.python, source.python, string.regexp.quoted.triple.python
"""           : punctuation.definition.string.end.python, source.python, string.regexp.quoted.triple.python
a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
R             : source.python, storage.type.string.python, string.quoted.multi.raw.python
"""           : punctuation.definition.string.begin.python, source.python, string.quoted.multi.raw.python
    (?x)        # not a : source.python, string.quoted.multi.raw.python
        foo     # comment : source.python, string.quoted.multi.raw.python
"""           : punctuation.definition.string.end.python, source.python, string.quoted.multi.raw.python
