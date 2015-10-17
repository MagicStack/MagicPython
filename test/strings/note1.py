a = 'XXX FIXME NB TODO'
a = r'XXX FIXME NB TODO'
a = b'XXX FIXME NB TODO'



a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
XXX FIXME NB TODO : source.python, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
r             : source.python, storage.type.string.python, string.regexp.quoted.python
'             : punctuation.definition.string.begin.python, source.python, string.regexp.quoted.python
XXX FIXME NB TODO : source.python, string.regexp.quoted.python
'             : punctuation.definition.string.end.python, source.python, string.regexp.quoted.python
a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
b             : source.python, storage.type.string.python, string.quoted.binary.single.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.binary.single.python
XXX FIXME NB TODO : source.python, string.quoted.binary.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.binary.single.python
