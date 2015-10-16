a = 'qqqwww'
a = ' { '
a = 'qqq{0:{widt' + 'h}{base}}www'




a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.single.python
qqqwww        : source.python, string.quoted.single.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.single.python
a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.single.python
 {            : source.python, string.quoted.single.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.single.python
a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.single.python
qqq{0:{widt   : source.python, string.quoted.single.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.single.python
              : source.python
+             : keyword.operator.python, source.python
              : source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.single.python
h}            : source.python, string.quoted.single.single.python
{base}        : constant.character.format.python, source.python, string.quoted.single.single.python
}www          : source.python, string.quoted.single.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.single.python
