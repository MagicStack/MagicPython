a. #foo
a.
#foo
a. \
#foo
a. 'bar'
a.
'bar'
a. \
'bar'




a             : source.python
.             : meta.member.access.python, punctuation.separator.period.python, source.python
              : meta.member.access.python, source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
foo           : comment.line.number-sign.python, source.python
a             : source.python
.             : meta.member.access.python, punctuation.separator.period.python, source.python
              : meta.member.access.python, source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
foo           : comment.line.number-sign.python, source.python
a             : source.python
.             : meta.member.access.python, punctuation.separator.period.python, source.python
              : meta.member.access.python, source.python
\             : meta.member.access.python, punctuation.separator.continuation.line.python, source.python
              : meta.member.access.python, source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
foo           : comment.line.number-sign.python, source.python
a             : source.python
.             : meta.member.access.python, punctuation.separator.period.python, source.python
              : meta.member.access.python, source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
bar           : source.python, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
a             : source.python
.             : meta.member.access.python, punctuation.separator.period.python, source.python
              : meta.member.access.python, source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.single.python
bar           : source.python, string.quoted.docstring.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.docstring.single.python
a             : source.python
.             : meta.member.access.python, punctuation.separator.period.python, source.python
              : meta.member.access.python, source.python
\             : meta.member.access.python, punctuation.separator.continuation.line.python, source.python
              : meta.member.access.python, source.python
'             : meta.member.access.python, punctuation.definition.string.begin.python, source.python, string.quoted.single.python
bar           : meta.member.access.python, source.python, string.quoted.single.python
'             : meta.member.access.python, punctuation.definition.string.end.python, source.python, string.quoted.single.python
