f"{} {  }"
f"""{}
{  }
"""





f             : meta.fstring.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.quoted.single.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
              : meta.fstring.python, source.python, string.interpolated.python, string.quoted.single.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
              : invalid.illegal.brace.python, meta.fstring.python, source.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
"             : meta.fstring.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.single.python
f             : meta.fstring.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.multi.python
"""           : meta.fstring.python, punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.quoted.multi.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
              : meta.fstring.python, source.python, string.interpolated.python, string.quoted.multi.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
              : invalid.illegal.brace.python, meta.fstring.python, source.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
              : meta.fstring.python, source.python, string.interpolated.python, string.quoted.multi.python
"""           : meta.fstring.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.multi.python
