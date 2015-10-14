(?x)
    (?:not) (foo)
        .* (?P<bar>BAR)
    \1 (?P=bar)



(?x)          : source.regexp, storage.modifier.flag.regexp
              : source.regexp
(?:           : punctuation.parenthesis.non-capturing.begin.regexp support.other.parenthesis.regexp, source.regexp
not           : source.regexp
)             : punctuation.parenthesis.non-capturing.end.regexp support.other.parenthesis.regexp, source.regexp
              : source.regexp
(             : punctuation.parenthesis.begin.regexp support.other.parenthesis.regexp, source.regexp
foo           : source.regexp
)             : punctuation.parenthesis.end.regexp support.other.parenthesis.regexp, source.regexp
              : source.regexp
.             : source.regexp, support.other.match.any.regexp
*             : keyword.operator.quantifier.regexp, source.regexp
              : source.regexp
(             : meta.named.regexp, punctuation.parenthesis.named.begin.regexp support.other.parenthesis.regexp, source.regexp
?P<bar>       : entity.name.tag.named.group.regexp, meta.named.regexp, source.regexp
BAR           : meta.named.regexp, source.regexp
)             : meta.named.regexp, punctuation.parenthesis.named.end.regexp support.other.parenthesis.regexp, source.regexp
              : source.regexp
\1            : entity.name.tag.backreference.regexp, meta.backreference.regexp, source.regexp
              : source.regexp
(             : meta.backreference.named.regexp, punctuation.parenthesis.backreference.named.begin.regexp support.other.parenthesis.regexp, source.regexp
?P=bar        : entity.name.tag.named.backreference.regexp, meta.backreference.named.regexp, source.regexp
)             : meta.backreference.named.regexp, punctuation.parenthesis.backreference.named.end.regexp support.other.parenthesis.regexp, source.regexp
