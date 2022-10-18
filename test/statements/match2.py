match point:
    case Point(x=0, y=0):
        print("Origin is the point's location.")
    case Point(x=0, y=y):
        print(f"The point is on the y-axis.")
    case Point(x=x, y=0):
        print(f"The point is on the x-axis.")
    case Point():
        print("The point is located somewhere else on the plane.")
    case _:
        print("Not a point")



match         : keyword.control.flow.python, source.python
              : source.python
point         : source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
case          : keyword.control.flow.python, source.python
              : source.python
Point         : meta.function-call.generic.python, meta.function-call.python, source.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
x             : meta.function-call.arguments.python, meta.function-call.python, source.python, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, source.python
0             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, source.python
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python
y             : meta.function-call.arguments.python, meta.function-call.python, source.python, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, source.python
0             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
print         : meta.function-call.python, source.python, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.python, string.quoted.single.python
Origin is the point's location. : meta.function-call.arguments.python, meta.function-call.python, source.python, string.quoted.single.python
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.python, string.quoted.single.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
              : source.python
case          : keyword.control.flow.python, source.python
              : source.python
Point         : meta.function-call.generic.python, meta.function-call.python, source.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
x             : meta.function-call.arguments.python, meta.function-call.python, source.python, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, source.python
0             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, source.python
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python
y             : meta.function-call.arguments.python, meta.function-call.python, source.python, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, source.python
y             : meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
print         : meta.function-call.python, source.python, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
f             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.quoted.single.python
The point is on the y-axis. : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.single.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
              : source.python
case          : keyword.control.flow.python, source.python
              : source.python
Point         : meta.function-call.generic.python, meta.function-call.python, source.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
x             : meta.function-call.arguments.python, meta.function-call.python, source.python, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, source.python
x             : meta.function-call.arguments.python, meta.function-call.python, source.python
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python
y             : meta.function-call.arguments.python, meta.function-call.python, source.python, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, source.python
0             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
print         : meta.function-call.python, source.python, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
f             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.quoted.single.python
The point is on the x-axis. : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.single.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
              : source.python
case          : keyword.control.flow.python, source.python
              : source.python
Point         : meta.function-call.generic.python, meta.function-call.python, source.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
print         : meta.function-call.python, source.python, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.python, string.quoted.single.python
The point is located somewhere else on the plane. : meta.function-call.arguments.python, meta.function-call.python, source.python, string.quoted.single.python
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.python, string.quoted.single.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
              : source.python
case          : keyword.control.flow.python, source.python
              : source.python
_             : source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
print         : meta.function-call.python, source.python, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.python, string.quoted.single.python
Not a point   : meta.function-call.arguments.python, meta.function-call.python, source.python, string.quoted.single.python
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.python, string.quoted.single.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
