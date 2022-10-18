match points:
    case []:
        print("No points in the list.")
    case [Point(0, 0)]:
        print("The origin is the only point in the list.")
    case [Point(x, y)]:
        print(f"A single point is in the list.")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two points on the Y axis are in the list.")
    case _:
        print("Something else is found in the list.")



match         : keyword.control.flow.python, source.python
              : source.python
points        : source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
case          : keyword.control.flow.python, source.python
              : source.python
[             : punctuation.definition.list.begin.python, source.python
]             : punctuation.definition.list.end.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
print         : meta.function-call.python, source.python, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.python, string.quoted.single.python
No points in the list. : meta.function-call.arguments.python, meta.function-call.python, source.python, string.quoted.single.python
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.python, string.quoted.single.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
              : source.python
case          : keyword.control.flow.python, source.python
              : source.python
[             : punctuation.definition.list.begin.python, source.python
Point         : meta.function-call.generic.python, meta.function-call.python, source.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
0             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, source.python
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python
0             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
]             : punctuation.definition.list.end.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
print         : meta.function-call.python, source.python, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.python, string.quoted.single.python
The origin is the only point in the list. : meta.function-call.arguments.python, meta.function-call.python, source.python, string.quoted.single.python
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.python, string.quoted.single.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
              : source.python
case          : keyword.control.flow.python, source.python
              : source.python
[             : punctuation.definition.list.begin.python, source.python
Point         : meta.function-call.generic.python, meta.function-call.python, source.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
x             : meta.function-call.arguments.python, meta.function-call.python, source.python
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python
y             : meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
]             : punctuation.definition.list.end.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
print         : meta.function-call.python, source.python, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
f             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.quoted.single.python
A single point is in the list. : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.single.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
              : source.python
case          : keyword.control.flow.python, source.python
              : source.python
[             : punctuation.definition.list.begin.python, source.python
Point         : meta.function-call.generic.python, meta.function-call.python, source.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
0             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, source.python
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python
y1            : meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
,             : punctuation.separator.element.python, source.python
              : source.python
Point         : meta.function-call.generic.python, meta.function-call.python, source.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
0             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, source.python
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python
y2            : meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
]             : punctuation.definition.list.end.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
print         : meta.function-call.python, source.python, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
f             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.quoted.single.python
Two points on the Y axis are in the list. : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.single.python
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
Something else is found in the list. : meta.function-call.arguments.python, meta.function-call.python, source.python, string.quoted.single.python
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.python, string.quoted.single.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
