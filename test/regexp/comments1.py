a = r'''foo[abc] # comment'''



a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
r             : source.python, storage.type.string.python, string.regexp.quoted.triple.python
'''           : punctuation.definition.string.begin.python, source.python, string.regexp.quoted.triple.python
foo           : source.python, string.regexp.quoted.triple.python
[             : constant.other.set.regexp, meta.character.set.regexp, punctuation.character.set.begin.regexp, source.python, string.regexp.quoted.triple.python
a             : constant.character.set.regexp, meta.character.set.regexp, source.python, string.regexp.quoted.triple.python
b             : constant.character.set.regexp, meta.character.set.regexp, source.python, string.regexp.quoted.triple.python
c             : constant.character.set.regexp, meta.character.set.regexp, source.python, string.regexp.quoted.triple.python
]             : constant.other.set.regexp, meta.character.set.regexp, punctuation.character.set.end.regexp, source.python, string.regexp.quoted.triple.python
              : source.python, string.regexp.quoted.triple.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python, string.regexp.quoted.triple.python
 comment      : comment.line.number-sign.python, source.python, string.regexp.quoted.triple.python
'''           : punctuation.definition.string.end.python, source.python, string.regexp.quoted.triple.python
