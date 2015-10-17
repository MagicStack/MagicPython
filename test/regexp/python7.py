a = r'('
1

a = r"(?="
1

a = r"""(?:
"""
1

a = r'''[
'''
1



a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
r             : source.python, storage.type.string.python, string.regexp.quoted.python
'             : punctuation.definition.string.begin.python, source.python, string.regexp.quoted.python
(             : punctuation.parenthesis.begin.regexp support.other.parenthesis.regexp, source.python, string.regexp.quoted.python
'             : punctuation.definition.string.end.python, source.python, string.regexp.quoted.python
1             : constant.numeric.dec.python, source.python
              : source.python
a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
r             : source.python, storage.type.string.python, string.regexp.quoted.python
"             : punctuation.definition.string.begin.python, source.python, string.regexp.quoted.python
(             : keyword.operator.lookahead.regexp, punctuation.parenthesis.lookahead.begin.regexp, source.python, string.regexp.quoted.python
?=            : keyword.operator.lookahead.regexp, source.python, string.regexp.quoted.python
"             : punctuation.definition.string.end.python, source.python, string.regexp.quoted.python
1             : constant.numeric.dec.python, source.python
              : source.python
a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
r             : source.python, storage.type.string.python, string.regexp.quoted.triple.python
"""           : punctuation.definition.string.begin.python, source.python, string.regexp.quoted.triple.python
(?:           : punctuation.parenthesis.non-capturing.begin.regexp support.other.parenthesis.regexp, source.python, string.regexp.quoted.triple.python
"""           : punctuation.definition.string.end.python, source.python, string.regexp.quoted.triple.python
1             : constant.numeric.dec.python, source.python
              : source.python
a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
r             : source.python, storage.type.string.python, string.regexp.quoted.triple.python
'''           : punctuation.definition.string.begin.python, source.python, string.regexp.quoted.triple.python
[             : constant.other.set.regexp punctuation.character.set.begin.regexp, meta.character.set.regexp, source.python, string.regexp.quoted.triple.python
'''           : punctuation.definition.string.end.python, source.python, string.regexp.quoted.triple.python
1             : constant.numeric.dec.python, source.python
