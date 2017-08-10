foo(?#NOTE:comment)bar



foo           : source.regexp.python
(?#           : comment.regexp, punctuation.comment.begin.regexp, source.regexp.python
NOTE          : comment.regexp, keyword.codetag.notation.python, source.regexp.python
:comment      : comment.regexp, source.regexp.python
)             : comment.regexp, punctuation.comment.end.regexp, source.regexp.python
bar           : source.regexp.python
