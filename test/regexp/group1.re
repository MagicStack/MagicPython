(?x)
    (?:not) (foo)
        .* (?P<bar>BAR)
    \1 (?P=bar)



(?x)          : source.regexp.python, storage.modifier.flag.regexp
              : source.regexp.python
(?:           : punctuation.parenthesis.non-capturing.begin.regexp support.other.parenthesis.regexp, source.regexp.python
not           : source.regexp.python
)             : punctuation.parenthesis.non-capturing.end.regexp support.other.parenthesis.regexp, source.regexp.python
              : source.regexp.python
(             : punctuation.parenthesis.begin.regexp support.other.parenthesis.regexp, source.regexp.python
foo           : source.regexp.python
)             : punctuation.parenthesis.end.regexp support.other.parenthesis.regexp, source.regexp.python
              : source.regexp.python
.             : source.regexp.python, support.other.match.any.regexp
*             : keyword.operator.quantifier.regexp, source.regexp.python
              : source.regexp.python
(             : meta.named.regexp, punctuation.parenthesis.named.begin.regexp support.other.parenthesis.regexp, source.regexp.python
?P<bar>       : entity.name.tag.named.group.regexp, meta.named.regexp, source.regexp.python
BAR           : meta.named.regexp, source.regexp.python
)             : meta.named.regexp, punctuation.parenthesis.named.end.regexp support.other.parenthesis.regexp, source.regexp.python
              : source.regexp.python
\1            : entity.name.tag.backreference.regexp, meta.backreference.regexp, source.regexp.python
              : source.regexp.python
(             : meta.backreference.named.regexp, punctuation.parenthesis.backreference.named.begin.regexp support.other.parenthesis.regexp, source.regexp.python
?P=bar        : entity.name.tag.named.backreference.regexp, meta.backreference.named.regexp, source.regexp.python
)             : meta.backreference.named.regexp, punctuation.parenthesis.backreference.named.end.regexp support.other.parenthesis.regexp, source.regexp.python
