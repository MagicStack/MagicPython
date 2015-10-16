a = """
multiline "unicode" string \

    \xf1 \u1234aaaa \U1234aaaa

    \N{BLACK SPADE SUIT}
"""



a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
"""           : punctuation.definition.string.begin.python, source.python, string.quoted.double.multi.python
multiline "unicode" string  : source.python, string.quoted.double.multi.python
\             : constant.language.python, source.python, string.quoted.double.multi.python
              : source.python, string.quoted.double.multi.python
              : source.python, string.quoted.double.multi.python
\xf1          : constant.character.python, source.python, string.quoted.double.multi.python
              : source.python, string.quoted.double.multi.python
\u1234        : constant.character.python, source.python, string.quoted.double.multi.python
aaaa          : source.python, string.quoted.double.multi.python
\U1234aaaa    : constant.character.python, source.python, string.quoted.double.multi.python
              : source.python, string.quoted.double.multi.python
              : source.python, string.quoted.double.multi.python
\N{BLACK SPADE SUIT} : constant.character.python, source.python, string.quoted.double.multi.python
"""           : punctuation.definition.string.end.python, source.python, string.quoted.double.multi.python
