f'foo {{{bar}}}'




f             : source.python, storage.type.string.python, string.quoted.single.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
foo           : source.python, string.quoted.single.python
{{            : constant.character.escape.python, source.python
{             : constant.character.format.placeholder.other.python, source.python
bar           : source.python
}             : constant.character.format.placeholder.other.python, source.python
}}            : constant.character.escape.python, source.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
