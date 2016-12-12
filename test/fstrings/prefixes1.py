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
f             : meta.fstring.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.single.python
'             : meta.fstring.python, punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.quoted.single.python
s t r         : meta.fstring.python, source.python, string.interpolated.python, string.quoted.single.python
'             : meta.fstring.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.single.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
f             : meta.fstring.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.quoted.single.python
s t r         : meta.fstring.python, source.python, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.single.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
F             : meta.fstring.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.single.python
'             : meta.fstring.python, punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.quoted.single.python
s t r         : meta.fstring.python, source.python, string.interpolated.python, string.quoted.single.python
'             : meta.fstring.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.single.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
F             : meta.fstring.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.quoted.single.python
s t r         : meta.fstring.python, source.python, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.single.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
f             : meta.fstring.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.multi.python
'''           : meta.fstring.python, punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.quoted.multi.python
s t r         : meta.fstring.python, source.python, string.interpolated.python, string.quoted.multi.python
'''           : meta.fstring.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.multi.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
F             : meta.fstring.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.multi.python
"""           : meta.fstring.python, punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.quoted.multi.python
s t r         : meta.fstring.python, source.python, string.interpolated.python, string.quoted.multi.python
"""           : meta.fstring.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.multi.python
