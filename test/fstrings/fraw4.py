a = rf'fo{{{2}}}'
a = rf'fo{{{bar}}}'
a = rf'fo{{2}}'





a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
rf            : meta.fstring.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.raw.single.python
'             : meta.fstring.python, punctuation.definition.string.begin.python, source.python, string.quoted.raw.single.python
fo            : meta.fstring.python, source.python, string.interpolated.python, string.quoted.raw.single.python
{{            : constant.character.escape.python, meta.fstring.python, source.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
2             : constant.numeric.dec.python, meta.fstring.python, source.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
}}            : constant.character.escape.python, meta.fstring.python, source.python
'             : meta.fstring.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.raw.single.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
rf            : meta.fstring.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.raw.single.python
'             : meta.fstring.python, punctuation.definition.string.begin.python, source.python, string.quoted.raw.single.python
fo            : meta.fstring.python, source.python, string.interpolated.python, string.quoted.raw.single.python
{{            : constant.character.escape.python, meta.fstring.python, source.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
bar           : meta.fstring.python, source.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
}}            : constant.character.escape.python, meta.fstring.python, source.python
'             : meta.fstring.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.raw.single.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
rf            : meta.fstring.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.raw.single.python
'             : meta.fstring.python, punctuation.definition.string.begin.python, source.python, string.quoted.raw.single.python
fo            : meta.fstring.python, source.python, string.interpolated.python, string.quoted.raw.single.python
{{            : constant.character.escape.python, meta.fstring.python, source.python
2             : meta.fstring.python, source.python, string.interpolated.python, string.quoted.raw.single.python
}}            : constant.character.escape.python, meta.fstring.python, source.python
'             : meta.fstring.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.raw.single.python
