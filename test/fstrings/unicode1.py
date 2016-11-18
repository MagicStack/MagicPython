a = f"""
multiline "unicode" string \

    \xf1 \u1234aaaa \U1234aaaa

    \N{BLACK SPADE SUIT}
"""



a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
f             : source.python, storage.type.string.python, string.quoted.multi.python
"""           : punctuation.definition.string.begin.python, source.python, string.quoted.multi.python
              : source.python, string.quoted.multi.python
multiline "unicode" string  : source.python, string.quoted.multi.python
\             : constant.language.python, source.python
              : source.python, string.quoted.multi.python
              : source.python, string.quoted.multi.python
              : source.python, string.quoted.multi.python
\xf1          : constant.character.escape.python, source.python
              : source.python, string.quoted.multi.python
\u1234        : constant.character.escape.python, source.python
aaaa          : source.python, string.quoted.multi.python
\U1234aaaa    : constant.character.escape.python, source.python
              : source.python, string.quoted.multi.python
              : source.python, string.quoted.multi.python
              : source.python, string.quoted.multi.python
\N{BLACK SPADE SUIT} : constant.character.escape.python, source.python
              : source.python, string.quoted.multi.python
"""           : punctuation.definition.string.end.python, source.python, string.quoted.multi.python
