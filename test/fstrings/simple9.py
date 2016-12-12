f'foo {{{bar}}}'




f             : meta.fstring.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.single.python
'             : meta.fstring.python, punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.quoted.single.python
foo           : meta.fstring.python, source.python, string.interpolated.python, string.quoted.single.python
{{            : constant.character.escape.python, meta.fstring.python, source.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
bar           : meta.fstring.python, source.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
}}            : constant.character.escape.python, meta.fstring.python, source.python
'             : meta.fstring.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.single.python
