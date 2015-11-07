a = r'foo#not a comment'
a = r'''
    (?x)        # multi-line regexp
        foo     # comment
'''
a = R'''
    (?x)        # not a
        foo     # comment
'''



a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
r             : source.python, storage.type.string.python, string.regexp.quoted.single.python
'             : punctuation.definition.string.begin.python, source.python, string.regexp.quoted.single.python
foo#not a comment : source.python, string.regexp.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.regexp.quoted.single.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
r             : source.python, storage.type.string.python, string.regexp.quoted.multi.python
'''           : punctuation.definition.string.begin.python, source.python, string.regexp.quoted.multi.python
              : source.python, string.regexp.quoted.multi.python
(?x)          : source.python, storage.modifier.flag.regexp, string.regexp.quoted.multi.python
              : source.python, string.regexp.quoted.multi.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python, string.regexp.quoted.multi.python
 multi-line regexp : comment.line.number-sign.python, source.python, string.regexp.quoted.multi.python
        foo      : source.python, string.regexp.quoted.multi.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python, string.regexp.quoted.multi.python
 comment      : comment.line.number-sign.python, source.python, string.regexp.quoted.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.regexp.quoted.multi.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
R             : source.python, storage.type.string.python, string.quoted.raw.multi.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.raw.multi.python
    (?x)        # not a : source.python, string.quoted.raw.multi.python
        foo     # comment : source.python, string.quoted.raw.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.raw.multi.python
