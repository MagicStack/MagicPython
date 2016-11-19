f"{} {  }"
f"""{}
{  }
"""





f             : source.python, storage.type.string.python, string.quoted.single.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
{}            : invalid.illegal.brace.python, source.python
              : source.python, string.quoted.single.python
{  }          : invalid.illegal.brace.python, source.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
f             : source.python, storage.type.string.python, string.quoted.multi.python
"""           : punctuation.definition.string.begin.python, source.python, string.quoted.multi.python
{}            : invalid.illegal.brace.python, source.python
              : source.python, string.quoted.multi.python
{  }          : invalid.illegal.brace.python, source.python
              : source.python, string.quoted.multi.python
"""           : punctuation.definition.string.end.python, source.python, string.quoted.multi.python
