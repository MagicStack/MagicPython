f"result: {value:{60}.{16!s:2}{'qwerty'
[2]}}"
# comment



f             : meta.fstring.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.quoted.single.python
result:       : meta.fstring.python, source.python, string.interpolated.python, string.quoted.single.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
value         : meta.fstring.python, source.python
:             : meta.fstring.python, source.python, storage.type.format.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
60            : constant.numeric.dec.python, meta.fstring.python, source.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
.             : meta.fstring.python, source.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
16            : constant.numeric.dec.python, meta.fstring.python, source.python
!s            : meta.fstring.python, source.python, storage.type.format.python
:2            : meta.fstring.python, source.python, storage.type.format.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
'             : meta.fstring.python, punctuation.definition.string.begin.python, source.python, string.quoted.single.python
qwerty        : meta.fstring.python, source.python, string.quoted.single.python
'             : meta.fstring.python, punctuation.definition.string.end.python, source.python, string.quoted.single.python
              : invalid.illegal.newline.python, meta.fstring.python, source.python
[             : punctuation.definition.list.begin.python, source.python
2             : constant.numeric.dec.python, source.python
]             : punctuation.definition.list.end.python, source.python
}}            : source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
              : invalid.illegal.newline.python, source.python, string.quoted.single.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 comment      : comment.line.number-sign.python, source.python
