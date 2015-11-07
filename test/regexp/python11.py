a = r"""
    (?x)        # multi-XXXline XXX regexp
        foo     (?# comm TODOent TODO)
        foo     # type: int
        foo     (?# type: int)
"""



a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
r             : source.python, storage.type.string.python, string.regexp.quoted.multi.python
"""           : punctuation.definition.string.begin.python, source.python, string.regexp.quoted.multi.python
              : source.python, string.regexp.quoted.multi.python
(?x)          : source.python, storage.modifier.flag.regexp, string.regexp.quoted.multi.python
              : source.python, string.regexp.quoted.multi.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python, string.regexp.quoted.multi.python
 multi-XXXline  : comment.line.number-sign.python, source.python, string.regexp.quoted.multi.python
XXX           : comment.line.number-sign.python, keyword.codetag.notation.python, source.python, string.regexp.quoted.multi.python
 regexp       : comment.line.number-sign.python, source.python, string.regexp.quoted.multi.python
        foo      : source.python, string.regexp.quoted.multi.python
(?#           : comment.regexp, punctuation.comment.begin.regexp, source.python, string.regexp.quoted.multi.python
 comm TODOent  : comment.regexp, source.python, string.regexp.quoted.multi.python
TODO          : comment.regexp, keyword.codetag.notation.python, source.python, string.regexp.quoted.multi.python
)             : comment.regexp, punctuation.comment.end.regexp, source.python, string.regexp.quoted.multi.python
        foo      : source.python, string.regexp.quoted.multi.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python, string.regexp.quoted.multi.python
 type: int    : comment.line.number-sign.python, source.python, string.regexp.quoted.multi.python
        foo      : source.python, string.regexp.quoted.multi.python
(?#           : comment.regexp, punctuation.comment.begin.regexp, source.python, string.regexp.quoted.multi.python
 type: int    : comment.regexp, source.python, string.regexp.quoted.multi.python
)             : comment.regexp, punctuation.comment.end.regexp, source.python, string.regexp.quoted.multi.python
"""           : punctuation.definition.string.end.python, source.python, string.regexp.quoted.multi.python
