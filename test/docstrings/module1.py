'''TEST'''
r'''TEST'''
R'''TEST'''

u'''TEST'''
U'''TEST'''
b'''TEST'''
B'''TEST'''



'''           : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.multi.python
TEST          : source.python, string.quoted.docstring.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.docstring.multi.python
r             : source.python, storage.type.string.python, string.quoted.docstring.raw.multi.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.raw.multi.python
TEST          : source.python, string.quoted.docstring.raw.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.docstring.raw.multi.python
R             : source.python, storage.type.string.python, string.quoted.docstring.raw.multi.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.raw.multi.python
TEST          : source.python, string.quoted.docstring.raw.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.docstring.raw.multi.python
              : source.python
u             : source.python, storage.type.string.python, string.quoted.multi.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.multi.python
TEST          : source.python, string.quoted.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.multi.python
U             : source.python, storage.type.string.python, string.quoted.multi.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.multi.python
TEST          : source.python, string.quoted.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.multi.python
b             : source.python, storage.type.string.python, string.quoted.binary.multi.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.binary.multi.python
TEST          : source.python, string.quoted.binary.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.binary.multi.python
B             : source.python, storage.type.string.python, string.quoted.binary.multi.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.binary.multi.python
TEST          : source.python, string.quoted.binary.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.binary.multi.python
