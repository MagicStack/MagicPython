foo(?!bar)



foo           : source.regexp.python
(             : keyword.operator.lookahead.negative.regexp, punctuation.parenthesis.lookahead.begin.regexp, source.regexp.python
?!            : keyword.operator.lookahead.negative.regexp, source.regexp.python
bar           : source.regexp.python
)             : punctuation.parenthesis.lookahead.end.regexp keyword.operator.lookahead.negative.regexp, source.regexp.python
