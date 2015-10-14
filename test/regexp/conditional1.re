(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)



(             : punctuation.parenthesis.begin.regexp support.other.parenthesis.regexp, source.regexp.python
<             : source.regexp.python
)             : punctuation.parenthesis.end.regexp support.other.parenthesis.regexp, source.regexp.python
?             : keyword.operator.quantifier.regexp, source.regexp.python
(             : punctuation.parenthesis.begin.regexp support.other.parenthesis.regexp, source.regexp.python
\w            : source.regexp.python, support.other.escape.special.regexp
+             : keyword.operator.quantifier.regexp, source.regexp.python
@             : source.regexp.python
\w            : source.regexp.python, support.other.escape.special.regexp
+             : keyword.operator.quantifier.regexp, source.regexp.python
(?:           : punctuation.parenthesis.non-capturing.begin.regexp support.other.parenthesis.regexp, source.regexp.python
\.            : constant.character.escape.regexp, source.regexp.python
\w            : source.regexp.python, support.other.escape.special.regexp
+             : keyword.operator.quantifier.regexp, source.regexp.python
)             : punctuation.parenthesis.non-capturing.end.regexp support.other.parenthesis.regexp, source.regexp.python
+             : keyword.operator.quantifier.regexp, source.regexp.python
)             : punctuation.parenthesis.end.regexp support.other.parenthesis.regexp, source.regexp.python
(             : keyword.operator.conditional.regexp, punctuation.parenthesis.conditional.begin.regexp, source.regexp.python
?(1)          : keyword.operator.conditional.regexp, source.regexp.python
>             : source.regexp.python
|             : keyword.operator.disjunction.regexp, source.regexp.python
$             : source.regexp.python, support.other.match.end.regexp
)             : punctuation.parenthesis.conditional.end.regexp keyword.operator.conditional.negative.regexp, source.regexp.python
