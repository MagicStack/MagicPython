a = 'qqq{0:{width}{base}}www'
a = 'qqq{0:$20}www'
a = 'qqq{0}www'




a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.single.python
qqq           : source.python, string.quoted.single.single.python
{0            : constant.character.format.python, source.python, string.quoted.single.single.python
:             : constant.character.format.python, source.python, string.quoted.single.single.python, support.other.format.python
{width}       : constant.character.format.python, source.python, string.quoted.single.single.python
{base}        : constant.character.format.python, source.python, string.quoted.single.single.python
}             : constant.character.format.python, source.python, string.quoted.single.single.python
www           : source.python, string.quoted.single.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.single.python
a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.single.python
qqq           : source.python, string.quoted.single.single.python
{0            : constant.character.format.python, source.python, string.quoted.single.single.python
:             : constant.character.format.python, source.python, string.quoted.single.single.python, support.other.format.python
$20           : constant.character.format.python, source.python, string.quoted.single.single.python
}             : constant.character.format.python, source.python, string.quoted.single.single.python
www           : source.python, string.quoted.single.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.single.python
a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.single.python
qqq           : source.python, string.quoted.single.single.python
{0}           : constant.character.format.python, source.python, string.quoted.single.single.python
www           : source.python, string.quoted.single.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.single.python
