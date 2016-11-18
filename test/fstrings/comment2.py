f'''
    prefix{10 # comment, perfectly legal
    } suffix'''




f             : source.python, storage.type.string.python, string.quoted.multi.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.multi.python
              : source.python, string.quoted.multi.python
    prefix    : source.python, string.quoted.multi.python
{             : constant.character.format.placeholder.other.python, source.python
10            : constant.numeric.dec.python, source.python
              : source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 comment, perfectly legal : comment.line.number-sign.python, source.python
              : source.python
}             : constant.character.format.placeholder.other.python, source.python
 suffix       : source.python, string.quoted.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.multi.python
