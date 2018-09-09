'implicit ' "concatenation"

'''implicit
''' 'concatenation'

'''implicit
''' """
concatenation
"""

'implicit' '''
concatenation
'''



'             : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.single.python
implicit      : source.python, string.quoted.docstring.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.docstring.single.python
              : source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.single.python
concatenation : source.python, string.quoted.docstring.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.docstring.single.python
              : source.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.multi.python
implicit      : source.python, string.quoted.docstring.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.docstring.multi.python
              : source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.single.python
concatenation : source.python, string.quoted.docstring.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.docstring.single.python
              : source.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.multi.python
implicit      : source.python, string.quoted.docstring.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.docstring.multi.python
              : source.python
"""           : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.multi.python
concatenation : source.python, string.quoted.docstring.multi.python
"""           : punctuation.definition.string.end.python, source.python, string.quoted.docstring.multi.python
              : source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.single.python
implicit      : source.python, string.quoted.docstring.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.docstring.single.python
              : source.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.multi.python
concatenation : source.python, string.quoted.docstring.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.docstring.multi.python
