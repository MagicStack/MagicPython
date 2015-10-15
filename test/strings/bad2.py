b"bad \\ string
foo \' \" \a \b \c \f \n \r \t \v \5 \55 \555 \05 \005"

def foo(a=1): pass



b             : source.python, storage.type.string.python, string.quoted.double.single.binary.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.double.single.binary.python
bad           : source.python, string.quoted.double.single.binary.python
\\            : constant.character.python, source.python, string.quoted.double.single.binary.python
 string       : source.python, string.quoted.double.single.binary.python
foo           : source.python, string.quoted.double.single.binary.python
\'            : constant.character.python, source.python, string.quoted.double.single.binary.python
              : source.python, string.quoted.double.single.binary.python
\"            : constant.character.python, source.python, string.quoted.double.single.binary.python
              : source.python, string.quoted.double.single.binary.python
\a            : constant.character.python, source.python, string.quoted.double.single.binary.python
              : source.python, string.quoted.double.single.binary.python
\b            : constant.character.python, source.python, string.quoted.double.single.binary.python
 \c           : source.python, string.quoted.double.single.binary.python
\f            : constant.character.python, source.python, string.quoted.double.single.binary.python
              : source.python, string.quoted.double.single.binary.python
\n            : constant.character.python, source.python, string.quoted.double.single.binary.python
              : source.python, string.quoted.double.single.binary.python
\r            : constant.character.python, source.python, string.quoted.double.single.binary.python
              : source.python, string.quoted.double.single.binary.python
\t            : constant.character.python, source.python, string.quoted.double.single.binary.python
              : source.python, string.quoted.double.single.binary.python
\v            : constant.character.python, source.python, string.quoted.double.single.binary.python
              : source.python, string.quoted.double.single.binary.python
\5            : constant.character.python, source.python, string.quoted.double.single.binary.python
              : source.python, string.quoted.double.single.binary.python
\55           : constant.character.python, source.python, string.quoted.double.single.binary.python
              : source.python, string.quoted.double.single.binary.python
\555          : constant.character.python, source.python, string.quoted.double.single.binary.python
              : source.python, string.quoted.double.single.binary.python
\05           : constant.character.python, source.python, string.quoted.double.single.binary.python
              : source.python, string.quoted.double.single.binary.python
\005          : constant.character.python, source.python, string.quoted.double.single.binary.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.double.single.binary.python
              : source.python
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
