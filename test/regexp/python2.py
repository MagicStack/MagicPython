R'
    (?x)
        foo
'



R             : source.python, storage.type.string.python, string.quoted.single.raw.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.raw.python
              : invalid.illegal.newline.python, source.python, string.quoted.single.raw.python
              : source.python
(             : punctuation.parenthesis.begin.python, source.python
?             : invalid.illegal.character.python, source.python
x             : source.python
)             : punctuation.parenthesis.end.python, source.python
        foo   : source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
              : invalid.illegal.newline.python, source.python, string.quoted.single.python
