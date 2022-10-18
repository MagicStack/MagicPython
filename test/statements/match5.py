match command.split() if command else ['default']:
    ... # Other cases
    case ["north"] | ["go", "north"]:
        ... # handle case
    case ["get", obj] | ["pick", "up", *other] | ["pick", obj, "up"]:
        ... # handle case




match         : keyword.control.flow.python, source.python
              : source.python
command       : source.python
.             : meta.member.access.python, punctuation.separator.period.python, source.python
split         : meta.function-call.generic.python, meta.function-call.python, meta.member.access.python, source.python
(             : meta.function-call.python, meta.member.access.python, punctuation.definition.arguments.begin.python, source.python
)             : meta.function-call.python, meta.member.access.python, punctuation.definition.arguments.end.python, source.python
              : source.python
if            : keyword.control.flow.python, source.python
              : source.python
command       : source.python
              : source.python
else          : keyword.control.flow.python, source.python
              : source.python
[             : punctuation.definition.list.begin.python, source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
default       : source.python, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
]             : punctuation.definition.list.end.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
...           : constant.other.ellipsis.python, source.python
              : source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 Other cases  : comment.line.number-sign.python, source.python
              : source.python
case          : keyword.control.flow.python, source.python
              : source.python
[             : punctuation.definition.list.begin.python, source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
north         : source.python, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
]             : punctuation.definition.list.end.python, source.python
              : source.python
|             : keyword.operator.bitwise.python, source.python
              : source.python
[             : punctuation.definition.list.begin.python, source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
go            : source.python, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
,             : punctuation.separator.element.python, source.python
              : source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
north         : source.python, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
]             : punctuation.definition.list.end.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
...           : constant.other.ellipsis.python, source.python
              : source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 handle case  : comment.line.number-sign.python, source.python
              : source.python
case          : keyword.control.flow.python, source.python
              : source.python
[             : punctuation.definition.list.begin.python, source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
get           : source.python, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
,             : punctuation.separator.element.python, source.python
              : source.python
obj           : source.python
]             : punctuation.definition.list.end.python, source.python
              : source.python
|             : keyword.operator.bitwise.python, source.python
              : source.python
[             : punctuation.definition.list.begin.python, source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
pick          : source.python, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
,             : punctuation.separator.element.python, source.python
              : source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
up            : source.python, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
,             : punctuation.separator.element.python, source.python
              : source.python
*             : keyword.operator.arithmetic.python, source.python
other         : source.python
]             : punctuation.definition.list.end.python, source.python
              : source.python
|             : keyword.operator.bitwise.python, source.python
              : source.python
[             : punctuation.definition.list.begin.python, source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
pick          : source.python, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
,             : punctuation.separator.element.python, source.python
              : source.python
obj           : source.python
,             : punctuation.separator.element.python, source.python
              : source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
up            : source.python, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
]             : punctuation.definition.list.end.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
...           : constant.other.ellipsis.python, source.python
              : source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 handle case  : comment.line.number-sign.python, source.python
