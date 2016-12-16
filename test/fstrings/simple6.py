f'insane{42 + 9000}stuff{def aaa(): pass}'
# def aaa() must not be parsed as a valid declaration




f             : meta.fstring.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.single.python
'             : meta.fstring.python, punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.quoted.single.python
insane        : meta.fstring.python, source.python, string.interpolated.python, string.quoted.single.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
42            : constant.numeric.dec.python, meta.fstring.python, source.python
              : meta.fstring.python, source.python
+             : keyword.operator.arithmetic.python, meta.fstring.python, source.python
              : meta.fstring.python, source.python
9000          : constant.numeric.dec.python, meta.fstring.python, source.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
stuff         : meta.fstring.python, source.python, string.interpolated.python, string.quoted.single.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
def           : keyword.control.flow.python, meta.fstring.python, source.python
              : meta.fstring.python, source.python
aaa           : meta.fstring.python, meta.function-call.generic.python, meta.function-call.python, source.python
(             : meta.fstring.python, meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
)             : meta.fstring.python, meta.function-call.python, punctuation.definition.arguments.end.python, source.python
:             : meta.fstring.python, punctuation.separator.colon.python, source.python
              : meta.fstring.python, source.python
pass          : keyword.control.flow.python, meta.fstring.python, source.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
'             : meta.fstring.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.single.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 def aaa() must not be parsed as a valid declaration : comment.line.number-sign.python, source.python
