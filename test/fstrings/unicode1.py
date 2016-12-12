a = f"""
multiline "unicode" string \

    \xf1 \u1234aaaa \U1234aaaa

    \N{BLACK SPADE SUIT}
"""



a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
f             : meta.fstring.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.multi.python
"""           : meta.fstring.python, punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.quoted.multi.python
              : meta.fstring.python, source.python, string.interpolated.python, string.quoted.multi.python
multiline "unicode" string  : meta.fstring.python, source.python, string.interpolated.python, string.quoted.multi.python
\             : constant.language.python, meta.fstring.python, source.python
              : meta.fstring.python, source.python, string.interpolated.python, string.quoted.multi.python
              : meta.fstring.python, source.python, string.interpolated.python, string.quoted.multi.python
              : meta.fstring.python, source.python, string.interpolated.python, string.quoted.multi.python
\xf1          : constant.character.escape.python, meta.fstring.python, source.python
              : meta.fstring.python, source.python, string.interpolated.python, string.quoted.multi.python
\u1234        : constant.character.escape.python, meta.fstring.python, source.python
aaaa          : meta.fstring.python, source.python, string.interpolated.python, string.quoted.multi.python
\U1234aaaa    : constant.character.escape.python, meta.fstring.python, source.python
              : meta.fstring.python, source.python, string.interpolated.python, string.quoted.multi.python
              : meta.fstring.python, source.python, string.interpolated.python, string.quoted.multi.python
              : meta.fstring.python, source.python, string.interpolated.python, string.quoted.multi.python
\N{BLACK SPADE SUIT} : constant.character.escape.python, meta.fstring.python, source.python
              : meta.fstring.python, source.python, string.interpolated.python, string.quoted.multi.python
"""           : meta.fstring.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.multi.python
