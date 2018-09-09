a = b'%b' % b'foo'



a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
b             : source.python, storage.type.string.python, string.quoted.binary.single.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.binary.single.python
%b            : constant.character.format.placeholder.other.python, meta.format.percent.python, source.python, string.quoted.binary.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.binary.single.python
              : source.python
%             : keyword.operator.arithmetic.python, source.python
              : source.python
b             : source.python, storage.type.string.python, string.quoted.binary.single.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.binary.single.python
foo           : source.python, string.quoted.binary.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.binary.single.python
