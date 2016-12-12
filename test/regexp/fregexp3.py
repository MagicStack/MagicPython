rf'fo{2}'
rf"fo{2}"
rf'''fo{2}'''
rf"""fo{2}"""




rf            : source.python, storage.type.string.python, string.interpolated.python, string.regexp.quoted.single.python
'             : punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.regexp.quoted.single.python
fo            : source.python, string.interpolated.python, string.regexp.quoted.single.python
{2}           : source.python, string.interpolated.python, string.regexp.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.interpolated.python, string.regexp.quoted.single.python
rf            : source.python, storage.type.string.python, string.interpolated.python, string.regexp.quoted.single.python
"             : punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.regexp.quoted.single.python
fo            : source.python, string.interpolated.python, string.regexp.quoted.single.python
{2}           : source.python, string.interpolated.python, string.regexp.quoted.single.python
"             : punctuation.definition.string.end.python, source.python, string.interpolated.python, string.regexp.quoted.single.python
rf            : source.python, storage.type.string.python, string.interpolated.python, string.regexp.quoted.multi.python
'''           : punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.regexp.quoted.multi.python
fo            : source.python, string.interpolated.python, string.regexp.quoted.multi.python
{2}           : source.python, string.interpolated.python, string.regexp.quoted.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.interpolated.python, string.regexp.quoted.multi.python
rf            : source.python, storage.type.string.python, string.interpolated.python, string.regexp.quoted.multi.python
"""           : punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.regexp.quoted.multi.python
fo            : source.python, string.interpolated.python, string.regexp.quoted.multi.python
{2}           : source.python, string.interpolated.python, string.regexp.quoted.multi.python
"""           : punctuation.definition.string.end.python, source.python, string.interpolated.python, string.regexp.quoted.multi.python
