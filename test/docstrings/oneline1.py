'''>>> print("""docstring""")'''
async
""">>> print('''docstring''')"""
await
"""\n>>> print('''docstring''')"""
await
"""   >>> print('''docstring''')"""
await
""" 1  >>> print('''docstring''')"""
await



'''           : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.python
>>>           : keyword.control.flow.python, source.python, string.quoted.docstring.python
print("""docstring""") : source.python, string.quoted.docstring.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.docstring.python
async         : keyword.control.flow.python, source.python
"""           : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.python
>>>           : keyword.control.flow.python, source.python, string.quoted.docstring.python
print('''docstring''') : source.python, string.quoted.docstring.python
"""           : punctuation.definition.string.end.python, source.python, string.quoted.docstring.python
await         : keyword.operator.python, source.python
"""           : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.python
\n            : constant.character.python, source.python, string.quoted.docstring.python
>>> print('''docstring''') : source.python, string.quoted.docstring.python
"""           : punctuation.definition.string.end.python, source.python, string.quoted.docstring.python
await         : keyword.operator.python, source.python
"""           : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.python
              : source.python, string.quoted.docstring.python
>>>           : keyword.control.flow.python, source.python, string.quoted.docstring.python
print('''docstring''') : source.python, string.quoted.docstring.python
"""           : punctuation.definition.string.end.python, source.python, string.quoted.docstring.python
await         : keyword.operator.python, source.python
"""           : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.python
 1  >>> print('''docstring''') : source.python, string.quoted.docstring.python
"""           : punctuation.definition.string.end.python, source.python, string.quoted.docstring.python
await         : keyword.operator.python, source.python
