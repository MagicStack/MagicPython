rf"{} {  }"
rf"""{}
{  }
"""





rf            : source.python, storage.type.string.python, string.interpolated.python, string.regexp.quoted.single.python
"             : punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.regexp.quoted.single.python
{             : constant.character.format.placeholder.other.python, source.python, string.interpolated.python, string.regexp.quoted.single.python
}             : constant.character.format.placeholder.other.python, source.python, string.interpolated.python, string.regexp.quoted.single.python
              : source.python, string.interpolated.python, string.regexp.quoted.single.python
{             : constant.character.format.placeholder.other.python, source.python, string.interpolated.python, string.regexp.quoted.single.python
              : invalid.illegal.brace.python, source.python, string.interpolated.python, string.regexp.quoted.single.python
}             : constant.character.format.placeholder.other.python, source.python, string.interpolated.python, string.regexp.quoted.single.python
"             : punctuation.definition.string.end.python, source.python, string.interpolated.python, string.regexp.quoted.single.python
rf            : source.python, storage.type.string.python, string.interpolated.python, string.regexp.quoted.multi.python
"""           : punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.regexp.quoted.multi.python
{             : constant.character.format.placeholder.other.python, source.python, string.interpolated.python, string.regexp.quoted.multi.python
}             : constant.character.format.placeholder.other.python, source.python, string.interpolated.python, string.regexp.quoted.multi.python
{             : constant.character.format.placeholder.other.python, source.python, string.interpolated.python, string.regexp.quoted.multi.python
              : invalid.illegal.brace.python, source.python, string.interpolated.python, string.regexp.quoted.multi.python
}             : constant.character.format.placeholder.other.python, source.python, string.interpolated.python, string.regexp.quoted.multi.python
"""           : punctuation.definition.string.end.python, source.python, string.interpolated.python, string.regexp.quoted.multi.python
