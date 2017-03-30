a = 'qqq{:%Y-%m-%d %H:%M:%S}www'
a = 'qqq{0:{fill}{align}16}www'




a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
qqq           : source.python, string.quoted.single.python
{             : constant.character.format.placeholder.other.python, source.python, string.quoted.single.python
:             : constant.character.format.placeholder.other.python, source.python, storage.type.format.python, string.quoted.single.python
%Y-%m-%d %H:%M:%S : constant.character.format.placeholder.other.python, source.python, string.quoted.single.python
}             : constant.character.format.placeholder.other.python, source.python, string.quoted.single.python
www           : source.python, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
qqq           : source.python, string.quoted.single.python
{0            : constant.character.format.placeholder.other.python, source.python, string.quoted.single.python
:             : constant.character.format.placeholder.other.python, source.python, storage.type.format.python, string.quoted.single.python
{fill}        : constant.character.format.placeholder.other.python, source.python, string.quoted.single.python
{align}       : constant.character.format.placeholder.other.python, source.python, string.quoted.single.python
16            : constant.character.format.placeholder.other.python, source.python, string.quoted.single.python
}             : constant.character.format.placeholder.other.python, source.python, string.quoted.single.python
www           : source.python, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
