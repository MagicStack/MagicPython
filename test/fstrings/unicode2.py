a = f"""
multiline "unicode" string
    \N{BLACK SPADE SUIT} {foo+2}
"""



a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
f             : meta.fstring.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.multi.python
"""           : meta.fstring.python, punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.quoted.multi.python
              : meta.fstring.python, source.python, string.interpolated.python, string.quoted.multi.python
multiline "unicode" string : meta.fstring.python, source.python, string.interpolated.python, string.quoted.multi.python
              : meta.fstring.python, source.python, string.interpolated.python, string.quoted.multi.python
\N{BLACK SPADE SUIT} : constant.character.escape.python, meta.fstring.python, source.python
              : meta.fstring.python, source.python, string.interpolated.python, string.quoted.multi.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
foo           : meta.fstring.python, source.python
+             : keyword.operator.arithmetic.python, meta.fstring.python, source.python
2             : constant.numeric.dec.python, meta.fstring.python, source.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
              : meta.fstring.python, source.python, string.interpolated.python, string.quoted.multi.python
"""           : meta.fstring.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.multi.python
