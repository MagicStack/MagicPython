foo(?#comment)bar



foo           : source.regexp.python
(?#           : comment.regexp, punctuation.comments.begin.regexp, source.regexp.python
comment       : comment.regexp, source.regexp.python
)             : comment.regexp, punctuation.comments.end.regexp, source.regexp.python
bar           : source.regexp.python
