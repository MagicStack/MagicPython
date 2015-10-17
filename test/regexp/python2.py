a = r'
    (?x)
        foo
'



a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
r             : source.python, storage.type.string.python, string.regexp.quoted.python
'             : punctuation.definition.string.begin.python, source.python, string.regexp.quoted.python
              : invalid.illegal.newline.python, source.python, string.regexp.quoted.python
              : source.python
(             : punctuation.parenthesis.begin.python, source.python
?             : invalid.illegal.character.python, source.python
x             : source.python
)             : punctuation.parenthesis.end.python, source.python
        foo   : source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
              : invalid.illegal.newline.python, source.python, string.quoted.single.python
