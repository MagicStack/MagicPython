f'''
    prefix{10
    + 32} suffix'''




f             : meta.fstring.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.multi.python
'''           : meta.fstring.python, punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.quoted.multi.python
              : meta.fstring.python, source.python, string.interpolated.python, string.quoted.multi.python
    prefix    : meta.fstring.python, source.python, string.interpolated.python, string.quoted.multi.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
10            : constant.numeric.dec.python, meta.fstring.python, source.python
              : meta.fstring.python, source.python
+             : keyword.operator.arithmetic.python, meta.fstring.python, source.python
              : meta.fstring.python, source.python
32            : constant.numeric.dec.python, meta.fstring.python, source.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
 suffix       : meta.fstring.python, source.python, string.interpolated.python, string.quoted.multi.python
'''           : meta.fstring.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.multi.python
