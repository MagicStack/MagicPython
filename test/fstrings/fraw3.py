rf'fo{2}'
rf"fo{2}"
rf'''fo{2}'''
rf"""fo{2}"""




rf            : meta.fstring.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.raw.single.python
'             : meta.fstring.python, punctuation.definition.string.begin.python, source.python, string.quoted.raw.single.python
fo            : meta.fstring.python, source.python, string.interpolated.python, string.quoted.raw.single.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
2             : constant.numeric.dec.python, meta.fstring.python, source.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
'             : meta.fstring.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.raw.single.python
rf            : meta.fstring.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.raw.single.python
"             : meta.fstring.python, punctuation.definition.string.begin.python, source.python, string.quoted.raw.single.python
fo            : meta.fstring.python, source.python, string.interpolated.python, string.quoted.raw.single.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
2             : constant.numeric.dec.python, meta.fstring.python, source.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
"             : meta.fstring.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.raw.single.python
rf            : meta.fstring.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.raw.multi.python
'''           : meta.fstring.python, punctuation.definition.string.begin.python, source.python, string.quoted.raw.multi.python
fo            : meta.fstring.python, source.python, string.interpolated.python, string.quoted.raw.multi.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
2             : constant.numeric.dec.python, meta.fstring.python, source.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
'''           : meta.fstring.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.raw.multi.python
rf            : meta.fstring.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.raw.multi.python
"""           : meta.fstring.python, punctuation.definition.string.begin.python, source.python, string.quoted.raw.multi.python
fo            : meta.fstring.python, source.python, string.interpolated.python, string.quoted.raw.multi.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
2             : constant.numeric.dec.python, meta.fstring.python, source.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
"""           : meta.fstring.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.raw.multi.python
