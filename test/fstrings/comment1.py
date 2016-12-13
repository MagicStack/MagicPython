f'prefix{10 # comment, making the string technically illegal
def foo(): pass




f             : meta.fstring.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.single.python
'             : meta.fstring.python, punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.quoted.single.python
prefix        : meta.fstring.python, source.python, string.interpolated.python, string.quoted.single.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
10            : constant.numeric.dec.python, meta.fstring.python, source.python
 #            : meta.fstring.python, source.python
comment       : meta.fstring.python, source.python
,             : meta.fstring.python, punctuation.separator.element.python, source.python
              : meta.fstring.python, source.python
making        : meta.fstring.python, source.python
              : meta.fstring.python, source.python
the           : meta.fstring.python, source.python
              : meta.fstring.python, source.python
string        : meta.fstring.python, source.python
              : meta.fstring.python, source.python
technically   : meta.fstring.python, source.python
              : meta.fstring.python, source.python
illegal       : meta.fstring.python, source.python
              : invalid.illegal.newline.python, meta.fstring.python, source.python
def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
pass          : keyword.control.flow.python, source.python
