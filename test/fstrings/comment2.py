f'''
    prefix{10
    + 32} suffix'''




f             : source.python, storage.type.string.python, string.quoted.multi.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.multi.python
              : source.python, string.quoted.multi.python
    prefix    : source.python, string.quoted.multi.python
{             : constant.character.format.placeholder.other.python, source.python
10            : constant.numeric.dec.python, source.python
              : source.python
+             : keyword.operator.arithmetic.python, source.python
              : source.python
32            : constant.numeric.dec.python, source.python
}             : constant.character.format.placeholder.other.python, source.python
 suffix       : source.python, string.quoted.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.multi.python
