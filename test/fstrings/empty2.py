rf"{} {  }"
rf"""{}
{  }
"""





rf            : meta.fstring.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.raw.single.python
"             : meta.fstring.python, punctuation.definition.string.begin.python, source.python, string.quoted.raw.single.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
              : meta.fstring.python, source.python, string.interpolated.python, string.quoted.raw.single.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
              : invalid.illegal.brace.python, meta.fstring.python, source.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
"             : meta.fstring.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.raw.single.python
rf            : meta.fstring.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.raw.multi.python
"""           : meta.fstring.python, punctuation.definition.string.begin.python, source.python, string.quoted.raw.multi.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
              : meta.fstring.python, source.python, string.interpolated.python, string.quoted.raw.multi.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
              : invalid.illegal.brace.python, meta.fstring.python, source.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
              : meta.fstring.python, source.python, string.interpolated.python, string.quoted.raw.multi.python
"""           : meta.fstring.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.raw.multi.python
