"""
multiline "unicode" string \

    \xf1 \u1234aaaa \U1234aaaa

    \N{BLACK SPADE SUIT}
"""



"""           : source.python, string.quoted.triple.python
multiline "unicode" string  : source.python, string.quoted.triple.python
\             : constant.language.python, source.python, string.quoted.triple.python
              : source.python, string.quoted.triple.python
              : source.python, string.quoted.triple.python
\xf1          : constant.character.python, source.python, string.quoted.triple.python
              : source.python, string.quoted.triple.python
\u1234        : constant.character.python, source.python, string.quoted.triple.python
aaaa          : source.python, string.quoted.triple.python
\U1234aaaa    : constant.character.python, source.python, string.quoted.triple.python
              : source.python, string.quoted.triple.python
              : source.python, string.quoted.triple.python
\N{BLACK SPADE SUIT} : constant.character.python, source.python, string.quoted.triple.python
"""           : source.python, string.quoted.triple.python
