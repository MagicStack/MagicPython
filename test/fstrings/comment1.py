f'prefix{10 # comment, making the string technically illegal
def foo(): pass




f             : source.python, storage.type.string.python, string.quoted.single.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
prefix        : source.python, string.quoted.single.python
{             : constant.character.format.placeholder.other.python, source.python
10            : constant.numeric.dec.python, source.python
 #            : source.python
comment       : source.python
,             : source.python
making        : source.python
              : source.python
the           : source.python
              : source.python
string        : source.python
              : source.python
technically   : source.python
              : source.python
illegal       : source.python
              : invalid.illegal.newline.python, source.python
def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
pass          : keyword.control.flow.python, source.python
