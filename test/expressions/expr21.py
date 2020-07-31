while chunk := file.read(8192):
   process(chunk)
   y0 = (y1 := f(x))



while         : keyword.control.flow.python, source.python
              : source.python
chunk         : source.python
              : source.python
:=            : keyword.operator.assignment.python, source.python
              : source.python
file          : source.python, variable.legacy.builtin.python
.             : meta.member.access.python, punctuation.separator.period.python, source.python
read          : meta.function-call.generic.python, meta.function-call.python, meta.member.access.python, source.python
(             : meta.function-call.python, meta.member.access.python, punctuation.definition.arguments.begin.python, source.python
8192          : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, meta.member.access.python, source.python
)             : meta.function-call.python, meta.member.access.python, punctuation.definition.arguments.end.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
process       : meta.function-call.generic.python, meta.function-call.python, source.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
chunk         : meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
              : source.python
y0            : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
(             : punctuation.parenthesis.begin.python, source.python
y1            : source.python
              : source.python
:=            : keyword.operator.assignment.python, source.python
              : source.python
f             : meta.function-call.generic.python, meta.function-call.python, source.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
x             : meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
)             : punctuation.parenthesis.end.python, source.python
