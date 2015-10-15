"bad \\ string
foo \' \" \a \b \c \f \n \r \t \v \5 \55 \555 \05 \005"
def foo(a=1): pass



"             : punctuation.definition.string.begin.python, source.python, string.quoted.double.single.python
bad           : source.python, string.quoted.double.single.python
\\            : constant.character.python, source.python, string.quoted.double.single.python
 string       : source.python, string.quoted.double.single.python
foo           : source.python, string.quoted.double.single.python
\'            : constant.character.python, source.python, string.quoted.double.single.python
              : source.python, string.quoted.double.single.python
\"            : constant.character.python, source.python, string.quoted.double.single.python
              : source.python, string.quoted.double.single.python
\a            : constant.character.python, source.python, string.quoted.double.single.python
              : source.python, string.quoted.double.single.python
\b            : constant.character.python, source.python, string.quoted.double.single.python
 \c           : source.python, string.quoted.double.single.python
\f            : constant.character.python, source.python, string.quoted.double.single.python
              : source.python, string.quoted.double.single.python
\n            : constant.character.python, source.python, string.quoted.double.single.python
              : source.python, string.quoted.double.single.python
\r            : constant.character.python, source.python, string.quoted.double.single.python
              : source.python, string.quoted.double.single.python
\t            : constant.character.python, source.python, string.quoted.double.single.python
              : source.python, string.quoted.double.single.python
\v            : constant.character.python, source.python, string.quoted.double.single.python
              : source.python, string.quoted.double.single.python
\5            : constant.character.python, source.python, string.quoted.double.single.python
              : source.python, string.quoted.double.single.python
\55           : constant.character.python, source.python, string.quoted.double.single.python
              : source.python, string.quoted.double.single.python
\555          : constant.character.python, source.python, string.quoted.double.single.python
              : source.python, string.quoted.double.single.python
\05           : constant.character.python, source.python, string.quoted.double.single.python
              : source.python, string.quoted.double.single.python
\005          : constant.character.python, source.python, string.quoted.double.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.double.single.python
def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
a             : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.pyhton
=             : keyword.operator.python, meta.function.parameters.python, meta.function.python, source.python
1             : constant.numeric.dec.python, meta.function.parameters.python, meta.function.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
pass          : keyword.control.flow.python, source.python
