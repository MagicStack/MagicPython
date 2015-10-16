r'
    (?x)
        foo
'



r             : source.python, storage.type.string.python, string.regexp.quoted.single.python
'             : punctuation.definition.string.begin.python, source.python, string.regexp.quoted.single.python
              : invalid.illegal.newline.python, source.python, string.regexp.quoted.single.python
              : source.python
(             : punctuation.parenthesis.begin.python, source.python
?             : invalid.illegal.character.python, source.python
x             : source.python
)             : punctuation.parenthesis.end.python, source.python
        foo   : source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.single.python
              : invalid.illegal.newline.python, source.python, string.quoted.single.single.python
