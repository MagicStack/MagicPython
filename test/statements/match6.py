match (foo + bar):
    ... # cases
match [foo, bar]:
    ... # cases
match {foo, bar}:
    ... # cases




match         : keyword.control.flow.python, source.python
              : source.python
(             : punctuation.parenthesis.begin.python, source.python
foo           : source.python
              : source.python
+             : keyword.operator.arithmetic.python, source.python
              : source.python
bar           : source.python
)             : punctuation.parenthesis.end.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
...           : constant.other.ellipsis.python, source.python
              : source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 cases        : comment.line.number-sign.python, source.python
match         : keyword.control.flow.python, source.python
              : source.python
[             : punctuation.definition.list.begin.python, source.python
foo           : source.python
,             : punctuation.separator.element.python, source.python
              : source.python
bar           : source.python
]             : punctuation.definition.list.end.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
...           : constant.other.ellipsis.python, source.python
              : source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 cases        : comment.line.number-sign.python, source.python
match         : keyword.control.flow.python, source.python
              : source.python
{             : punctuation.definition.dict.begin.python, source.python
foo           : source.python
,             : punctuation.separator.element.python, source.python
              : source.python
bar           : source.python
}             : punctuation.definition.dict.end.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
...           : constant.other.ellipsis.python, source.python
              : source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 cases        : comment.line.number-sign.python, source.python