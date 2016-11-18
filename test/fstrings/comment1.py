f'prefix{10 # comment, making the string technically illegal
def foo(): pass




f             : source.python, storage.type.string.python, string.quoted.single.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
prefix        : source.python, string.quoted.single.python
{             : constant.character.format.placeholder.other.python, source.python
10            : constant.numeric.dec.python, source.python
              : source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 comment, making the string technically illegal : comment.line.number-sign.python, source.python
def           : keyword.control.flow.python, source.python
              : source.python
foo           : meta.function-call.generic.python, meta.function-call.python, source.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
:             : source.python, support.other.format.python
pass          : keyword.control.flow.python, source.python
