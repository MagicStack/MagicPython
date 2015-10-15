R"""
multiline "raw" string \

    \xf1 \u1234aaaa \U1234aaaa

    \N{BLACK SPADE SUIT}
"""



R             : source.python, storage.type.string.python, string.quoted.double.multi.raw.python
"""           : punctuation.definition.string.begin.python, source.python, string.quoted.double.multi.raw.python
multiline "raw" string \ : source.python, string.quoted.double.multi.raw.python
              : source.python, string.quoted.double.multi.raw.python
              : source.python, string.quoted.double.multi.raw.python
\x            : source.python, string.quoted.double.multi.raw.python
f1            : source.python, string.quoted.double.multi.raw.python
\u            : source.python, string.quoted.double.multi.raw.python
1234aaaa      : source.python, string.quoted.double.multi.raw.python
\U            : source.python, string.quoted.double.multi.raw.python
1234aaaa      : source.python, string.quoted.double.multi.raw.python
              : source.python, string.quoted.double.multi.raw.python
              : source.python, string.quoted.double.multi.raw.python
\N            : source.python, string.quoted.double.multi.raw.python
{BLACK SPADE SUIT} : constant.character.format.python, source.python, string.quoted.double.multi.raw.python
"""           : punctuation.definition.string.end.python, source.python, string.quoted.double.multi.raw.python
