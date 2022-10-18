match point:
    case Point(x, y) if x == y:
        print(f"The point is located on the diagonal Y=X.")
    case Point(x, y):
        print(f"Point is not on the diagonal.")




match         : keyword.control.flow.python, source.python
              : source.python
point         : source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
case          : keyword.control.flow.python, source.python
              : source.python
Point         : meta.function-call.generic.python, meta.function-call.python, source.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
x             : meta.function-call.arguments.python, meta.function-call.python, source.python
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python
y             : meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
              : source.python
if            : keyword.control.flow.python, source.python
              : source.python
x             : source.python
              : source.python
==            : keyword.operator.comparison.python, source.python
              : source.python
y             : source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
print         : meta.function-call.python, source.python, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
f             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.quoted.single.python
The point is located on the diagonal Y=X. : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.single.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
              : source.python
case          : keyword.control.flow.python, source.python
              : source.python
Point         : meta.function-call.generic.python, meta.function-call.python, source.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
x             : meta.function-call.arguments.python, meta.function-call.python, source.python
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python
y             : meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
print         : meta.function-call.python, source.python, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
f             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.quoted.single.python
Point is not on the diagonal. : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.single.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
