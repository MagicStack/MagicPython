a = f's t r'
a = f"s t r"
a = F's t r'
a = F"s t r"
a = f'''s t r'''
a = F"""s t r"""



a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
f             : source.python, storage.type.string.python, string.quoted.single.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
s t r         : source.python, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
f             : source.python, storage.type.string.python, string.quoted.single.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
s t r         : source.python, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
F             : source.python, storage.type.string.python, string.quoted.single.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
s t r         : source.python, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
F             : source.python, storage.type.string.python, string.quoted.single.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
s t r         : source.python, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
f             : source.python, storage.type.string.python, string.quoted.multi.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.multi.python
s t r         : source.python, string.quoted.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.multi.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
F             : source.python, storage.type.string.python, string.quoted.multi.python
"""           : punctuation.definition.string.begin.python, source.python, string.quoted.multi.python
s t r         : source.python, string.quoted.multi.python
"""           : punctuation.definition.string.end.python, source.python, string.quoted.multi.python
