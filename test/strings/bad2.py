a = b"bad \\ string
foo \' \" \a \b \c \f \n \r \t \v \5 \55 \555 \05 \005"

def foo(a=1): pass




a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
b             : source.python, storage.type.string.python, string.quoted.binary.single.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.binary.single.python
bad           : source.python, string.quoted.binary.single.python
\\            : constant.character.escape.python, source.python, string.quoted.binary.single.python
 string       : source.python, string.quoted.binary.single.python
              : invalid.illegal.newline.python, source.python, string.quoted.binary.single.python
foo           : source.python
              : source.python
\             : punctuation.separator.continuation.line.python, source.python
' \" \a \b \c \f \n \r \t \v \5 \55 \555 \05 \005" : invalid.illegal.line.continuation.python, source.python
              : source.python
def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
a             : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.python
=             : keyword.operator.python, meta.function.parameters.python, meta.function.python, source.python
1             : constant.numeric.dec.python, meta.function.parameters.python, meta.function.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
pass          : keyword.control.flow.python, source.python
