f"""result: {value:{60}.{16!s:2}{'qwerty'
[2]}}"""
def foo(): pass




f             : meta.fstring.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.multi.python
"""           : meta.fstring.python, punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.quoted.multi.python
result:       : meta.fstring.python, source.python, string.interpolated.python, string.quoted.multi.python
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
[             : meta.fstring.python, punctuation.definition.list.begin.python, source.python
2             : constant.numeric.dec.python, meta.fstring.python, source.python
]             : meta.fstring.python, punctuation.definition.list.end.python, source.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
"""           : meta.fstring.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.multi.python
def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
pass          : keyword.control.flow.python, source.python
