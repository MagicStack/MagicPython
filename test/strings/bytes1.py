b"""
multiline "binary" string \

    \xf1 \u1234aaaa \U1234aaaa

    \N{BLACK SPADE SUIT}
"""



b             : source.python, storage.type.string.python, string.quoted.triple.python
"""           : source.python, string.quoted.triple.python
multiline "binary" string  : source.python, string.quoted.triple.python
\             : constant.language.python, source.python, string.quoted.triple.python
              : source.python, string.quoted.triple.python
              : source.python, string.quoted.triple.python
\xf1          : constant.character.python, source.python, string.quoted.triple.python
 \u1234aaaa \U1234aaaa : source.python, string.quoted.triple.python
              : source.python, string.quoted.triple.python
    \N{BLACK SPADE SUIT} : source.python, string.quoted.triple.python
"""           : source.python, string.quoted.triple.python
