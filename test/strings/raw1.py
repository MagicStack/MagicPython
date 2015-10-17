a = R"""
multiline "raw" string \

    \xf1 \u1234aaaa \U1234aaaa

    \N{BLACK SPADE SUIT}
"""



a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
R             : source.python, storage.type.string.python, string.quoted.raw.multi.python
"""           : punctuation.definition.string.begin.python, source.python, string.quoted.raw.multi.python
multiline "raw" string \ : source.python, string.quoted.raw.multi.python
              : source.python, string.quoted.raw.multi.python
              : source.python, string.quoted.raw.multi.python
\x            : source.python, string.quoted.raw.multi.python
f1            : source.python, string.quoted.raw.multi.python
\u            : source.python, string.quoted.raw.multi.python
1234aaaa      : source.python, string.quoted.raw.multi.python
\U            : source.python, string.quoted.raw.multi.python
1234aaaa      : source.python, string.quoted.raw.multi.python
              : source.python, string.quoted.raw.multi.python
              : source.python, string.quoted.raw.multi.python
\N            : source.python, string.quoted.raw.multi.python
{BLACK SPADE SUIT} : constant.character.format.python, source.python, string.quoted.raw.multi.python
"""           : punctuation.definition.string.end.python, source.python, string.quoted.raw.multi.python
