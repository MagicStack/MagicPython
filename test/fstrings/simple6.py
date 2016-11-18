f'insane{42 + 9000}stuff{def aaa(): pass}'
# def aaa() must not be parsed as a valid declaration




f             : source.python, storage.type.string.python, string.quoted.single.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
insane        : source.python, string.quoted.single.python
{             : constant.character.format.placeholder.other.python, source.python
42            : constant.numeric.dec.python, source.python
              : source.python
+             : keyword.operator.arithmetic.python, source.python
              : source.python
9000          : constant.numeric.dec.python, source.python
}             : constant.character.format.placeholder.other.python, source.python
stuff         : source.python, string.quoted.single.python
{             : constant.character.format.placeholder.other.python, source.python
def           : keyword.control.flow.python, source.python
              : source.python
aaa           : meta.function-call.generic.python, meta.function-call.python, source.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
:             : source.python, support.other.format.python
pass          : keyword.control.flow.python, source.python
}             : constant.character.format.placeholder.other.python, source.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 def aaa() must not be parsed as a valid declaration : comment.line.number-sign.python, source.python
