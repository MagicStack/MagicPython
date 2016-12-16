some_number: int           # variable without initial value
some_list: List[int] = []  # variable with initial value



some_number   : source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
int           : source.python, support.type.python
              : source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 variable without initial value : comment.line.number-sign.python, source.python
some_list     : source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
List          : meta.item-access.python, source.python
[             : meta.item-access.python, punctuation.definition.arguments.begin.python, source.python
int           : meta.item-access.arguments.python, meta.item-access.python, source.python, support.type.python
]             : meta.item-access.python, punctuation.definition.arguments.end.python, source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
[             : punctuation.definition.list.begin.python, source.python
]             : punctuation.definition.list.end.python, source.python
              : source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 variable with initial value : comment.line.number-sign.python, source.python
