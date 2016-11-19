f'''
    prefix{10 # comment is still illegal here
    } suffix'''




f             : source.python, storage.type.string.python, string.quoted.multi.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.multi.python
              : source.python, string.quoted.multi.python
    prefix    : source.python, string.quoted.multi.python
{             : constant.character.format.placeholder.other.python, source.python
10            : constant.numeric.dec.python, source.python
 #            : source.python
comment       : source.python
              : source.python
is            : keyword.operator.logical.python, source.python
              : source.python
still         : source.python
              : source.python
illegal       : source.python
              : source.python
here          : source.python
              : source.python
}             : constant.character.format.placeholder.other.python, source.python
 suffix       : source.python, string.quoted.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.multi.python
