b"""
multiline "binary" string \

    \xf1 \u1234aaaa \U1234aaaa

    \N{BLACK SPADE SUIT}
"""



b             : source.python, storage.type.string.python, string.quoted.double.multi.binary.python
"""           : punctuation.definition.string.begin.python, source.python, string.quoted.double.multi.binary.python
multiline "binary" string  : source.python, string.quoted.double.multi.binary.python
\             : constant.language.python, source.python, string.quoted.double.multi.binary.python
              : source.python, string.quoted.double.multi.binary.python
              : source.python, string.quoted.double.multi.binary.python
\xf1          : constant.character.python, source.python, string.quoted.double.multi.binary.python
 \u1234aaaa \U1234aaaa : source.python, string.quoted.double.multi.binary.python
              : source.python, string.quoted.double.multi.binary.python
    \N{BLACK SPADE SUIT} : source.python, string.quoted.double.multi.binary.python
"""           : punctuation.definition.string.end.python, source.python, string.quoted.double.multi.binary.python
