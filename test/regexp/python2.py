a = r'
    (?x)
        foo
'



a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
r             : source.python, storage.type.string.python, string.regexp.quoted.single.python
'             : punctuation.definition.string.begin.python, source.python, string.regexp.quoted.single.python
              : invalid.illegal.newline.python, source.python, string.regexp.quoted.single.python
              : source.python
(             : punctuation.parenthesis.begin.python, source.python
?             : invalid.illegal.operator.python, source.python
x             : source.python
)             : punctuation.parenthesis.end.python, source.python
              : source.python
foo           : source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.single.python
              : invalid.illegal.newline.python, source.python, string.quoted.docstring.single.python
