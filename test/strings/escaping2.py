replace = {'"' : r'\"',
           "'" : r'\'',
           '\\': r'\\'}


replace       : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
{             : source.python
'             : source.python, string.quoted.single.python
"             : source.python, string.quoted.single.python
'             : source.python, string.quoted.single.python
 :            : source.python
r             : source.python, storage.type.string.python, string.quoted.single.raw.python
'             : source.python, string.quoted.single.raw.python
\"            : source.python, string.quoted.single.raw.python
'             : source.python, string.quoted.single.raw.python
,             : source.python
              : source.python
"             : source.python, string.quoted.double.python
'             : source.python, string.quoted.double.python
"             : source.python, string.quoted.double.python
 :            : source.python
r             : source.python, storage.type.string.python, string.quoted.single.raw.python
'             : source.python, string.quoted.single.raw.python
\'            : source.python, string.quoted.single.raw.python
'             : source.python, string.quoted.single.raw.python
,             : source.python
              : source.python
'             : source.python, string.quoted.single.python
\\            : constant.character.python, source.python, string.quoted.single.python
'             : source.python, string.quoted.single.python
:             : source.python
r             : source.python, storage.type.string.python, string.quoted.single.raw.python
'             : source.python, string.quoted.single.raw.python
\\            : source.python, string.quoted.single.raw.python
'             : source.python, string.quoted.single.raw.python
}             : source.python
