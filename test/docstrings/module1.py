'''TEST'''
r'''TEST'''
R'''TEST'''

u'''TEST'''
U'''TEST'''
b'''TEST'''
B'''TEST'''



'''           : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.python
TEST          : source.python, string.quoted.docstring.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.docstring.python
r             : source.python, storage.type.string.python, string.quoted.docstring.raw.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.raw.python
TEST          : source.python, string.quoted.docstring.raw.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.docstring.raw.python
R             : source.python, storage.type.string.python, string.quoted.docstring.raw.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.raw.python
TEST          : source.python, string.quoted.docstring.raw.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.docstring.raw.python
              : source.python
u             : source.python, storage.type.string.python, string.quoted.single.multi.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.single.multi.python
TEST          : source.python, string.quoted.single.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.single.multi.python
U             : source.python, storage.type.string.python, string.quoted.single.multi.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.single.multi.python
TEST          : source.python, string.quoted.single.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.single.multi.python
b             : source.python, storage.type.string.python, string.quoted.single.multi.binary.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.single.multi.binary.python
TEST          : source.python, string.quoted.single.multi.binary.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.single.multi.binary.python
B             : source.python, storage.type.string.python, string.quoted.single.multi.binary.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.single.multi.binary.python
TEST          : source.python, string.quoted.single.multi.binary.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.single.multi.binary.python
