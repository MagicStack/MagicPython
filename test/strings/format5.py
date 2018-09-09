a = 'qqq{0:{width}{base}}www'
a = 'qqq{0:$20}www'
a = 'qqq{0}www'




a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
qqq           : source.python, string.quoted.single.python
{0            : constant.character.format.placeholder.other.python, meta.format.brace.python, source.python, string.quoted.single.python
:             : constant.character.format.placeholder.other.python, meta.format.brace.python, source.python, storage.type.format.python, string.quoted.single.python
{width}{base}} : constant.character.format.placeholder.other.python, meta.format.brace.python, source.python, string.quoted.single.python
www           : source.python, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
qqq           : source.python, string.quoted.single.python
{0            : constant.character.format.placeholder.other.python, meta.format.brace.python, source.python, string.quoted.single.python
:             : constant.character.format.placeholder.other.python, meta.format.brace.python, source.python, storage.type.format.python, string.quoted.single.python
$20}          : constant.character.format.placeholder.other.python, meta.format.brace.python, source.python, string.quoted.single.python
www           : source.python, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
qqq           : source.python, string.quoted.single.python
{0}           : constant.character.format.placeholder.other.python, meta.format.brace.python, source.python, string.quoted.single.python
www           : source.python, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
