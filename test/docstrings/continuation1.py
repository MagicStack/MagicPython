# not a docstring
a = \
r'''
>>> print(42)
a[wer]
'''

b = \
# docstring
r'''
>>> print()
a[wer]
'''



#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 not a docstring : comment.line.number-sign.python, source.python
a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
\             : separator.continuation.line.python, source.python
              : source.python
r             : source.python, storage.type.string.python, string.regexp.quoted.triple.python
'''           : punctuation.definition.string.begin.python, source.python, string.regexp.quoted.triple.python
>>> print     : source.python, string.regexp.quoted.triple.python
(             : punctuation.parenthesis.begin.regexp support.other.parenthesis.regexp, source.python, string.regexp.quoted.triple.python
42            : source.python, string.regexp.quoted.triple.python
)             : punctuation.parenthesis.end.regexp support.other.parenthesis.regexp, source.python, string.regexp.quoted.triple.python
a             : source.python, string.regexp.quoted.triple.python
[             : constant.other.set.regexp punctuation.character.set.begin.regexp, meta.character.set.regexp, source.python, string.regexp.quoted.triple.python
w             : constant.character.set.regexp, meta.character.set.regexp, source.python, string.regexp.quoted.triple.python
e             : constant.character.set.regexp, meta.character.set.regexp, source.python, string.regexp.quoted.triple.python
r             : constant.character.set.regexp, meta.character.set.regexp, source.python, string.regexp.quoted.triple.python
]             : constant.other.set.regexp punctuation.character.set.end.regexp, meta.character.set.regexp, source.python, string.regexp.quoted.triple.python
'''           : punctuation.definition.string.end.python, source.python, string.regexp.quoted.triple.python
              : source.python
b             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
\             : separator.continuation.line.python, source.python
              : source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 docstring    : comment.line.number-sign.python, source.python
r             : source.python, storage.type.string.python, string.quoted.docstring.raw.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.raw.python
>>>           : source.python, string.quoted.docstring.raw.python
              : source.python, string.quoted.docstring.raw.python
print         : meta.function-call.python, source.python, string.quoted.docstring.raw.python, support.function.builtin.python
(             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.arguments.begin.python, source.python, string.quoted.docstring.raw.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python, string.quoted.docstring.raw.python
a[wer]        : source.python, string.quoted.docstring.raw.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.docstring.raw.python
