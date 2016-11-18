f"result: {value:{60}.{16!s:2}{'qwerty'[2]}}"



f             : source.python, storage.type.string.python, string.quoted.single.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
result:       : source.python, string.quoted.single.python
{             : constant.character.format.placeholder.other.python, source.python
value         : source.python
:             : source.python, support.other.format.python
{             : punctuation.definition.dict.begin.python, source.python
60            : constant.numeric.dec.python, source.python
}             : punctuation.definition.dict.end.python, source.python
.             : source.python
{             : punctuation.definition.dict.begin.python, source.python
16            : constant.numeric.dec.python, source.python
!             : invalid.illegal.operator.python, source.python
s             : source.python
:             : source.python
2             : constant.numeric.dec.python, source.python
}             : punctuation.definition.dict.end.python, source.python
{             : punctuation.definition.dict.begin.python, source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
qwerty        : source.python, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
[             : punctuation.definition.list.begin.python, source.python
2             : constant.numeric.dec.python, source.python
]             : punctuation.definition.list.end.python, source.python
}             : punctuation.definition.dict.end.python, source.python
}             : constant.character.format.placeholder.other.python, source.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
