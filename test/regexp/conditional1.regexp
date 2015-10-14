(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)



(             : punctuation.parenthesis.begin.regexp support.other.parenthesis.regexp, source.regexp
<             : source.regexp
)             : punctuation.parenthesis.end.regexp support.other.parenthesis.regexp, source.regexp
?             : keyword.operator.quantifier.regexp, source.regexp
(             : punctuation.parenthesis.begin.regexp support.other.parenthesis.regexp, source.regexp
\w            : source.regexp, support.other.escape.special.regexp
+             : keyword.operator.quantifier.regexp, source.regexp
@             : source.regexp
\w            : source.regexp, support.other.escape.special.regexp
+             : keyword.operator.quantifier.regexp, source.regexp
(?:           : punctuation.parenthesis.non-capturing.begin.regexp support.other.parenthesis.regexp, source.regexp
\.            : constant.character.escape.regexp, source.regexp
\w            : source.regexp, support.other.escape.special.regexp
+             : keyword.operator.quantifier.regexp, source.regexp
)             : punctuation.parenthesis.non-capturing.end.regexp support.other.parenthesis.regexp, source.regexp
+             : keyword.operator.quantifier.regexp, source.regexp
)             : punctuation.parenthesis.end.regexp support.other.parenthesis.regexp, source.regexp
(             : keyword.operator.conditional.regexp, punctuation.parenthesis.conditional.begin.regexp, source.regexp
?(1)          : keyword.operator.conditional.regexp, source.regexp
>             : source.regexp
|             : keyword.operator.disjunction.regexp, source.regexp
$             : source.regexp, support.other.match.end.regexp
)             : punctuation.parenthesis.conditional.end.regexp keyword.operator.conditional.negative.regexp, source.regexp
