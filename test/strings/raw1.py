r"""
multiline "raw" string \

    \xf1 \u1234aaaa \U1234aaaa

    \N{BLACK SPADE SUIT}
"""



r             : source.python, storage.type.string.python, string.quoted.triple.raw.python
"""           : source.python, string.quoted.triple.raw.python
multiline "raw" string \ : source.python, string.quoted.triple.raw.python
              : source.python, string.quoted.triple.raw.python
              : source.python, string.quoted.triple.raw.python
\x            : source.python, string.quoted.triple.raw.python
f1            : source.python, string.quoted.triple.raw.python
\u            : source.python, string.quoted.triple.raw.python
1234aaaa      : source.python, string.quoted.triple.raw.python
\U            : source.python, string.quoted.triple.raw.python
1234aaaa      : source.python, string.quoted.triple.raw.python
              : source.python, string.quoted.triple.raw.python
              : source.python, string.quoted.triple.raw.python
\N            : source.python, string.quoted.triple.raw.python
{BLACK SPADE SUIT} : constant.character.format.python, source.python, string.quoted.triple.raw.python
"""           : source.python, string.quoted.triple.raw.python
