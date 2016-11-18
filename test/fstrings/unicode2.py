a = f"""
multiline "unicode" string
    \N{BLACK SPADE SUIT} {foo+2}
"""



a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
f             : source.python, storage.type.string.python, string.quoted.multi.python
"""           : punctuation.definition.string.begin.python, source.python, string.quoted.multi.python
              : source.python, string.quoted.multi.python
multiline "unicode" string : source.python, string.quoted.multi.python
              : source.python, string.quoted.multi.python
\N{BLACK SPADE SUIT} : constant.character.escape.python, source.python
              : source.python, string.quoted.multi.python
{             : constant.character.format.placeholder.other.python, source.python
foo           : source.python
+             : keyword.operator.arithmetic.python, source.python
2             : constant.numeric.dec.python, source.python
}             : constant.character.format.placeholder.other.python, source.python
              : source.python, string.quoted.multi.python
"""           : punctuation.definition.string.end.python, source.python, string.quoted.multi.python
