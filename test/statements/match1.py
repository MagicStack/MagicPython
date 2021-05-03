match status:
    case 100:
        pass
    case \
        200:
        pass
    case (
        300
    ):
        pass
    case [
        400
    ]:
        pass
    case {
        500: "",
    }:
        pass
    case Point(x, y) as p:
        pass
    case 600 | 700:
        pass
    case _:



match         : keyword.control.flow.python, source.python
              : source.python
status        : source.python
:             : punctuation.separator.colon.python, source.python
    case      : keyword.control.flow.python, source.python
              : source.python
100           : constant.numeric.dec.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
pass          : keyword.control.flow.python, source.python
    case      : keyword.control.flow.python, source.python
              : source.python
\             : punctuation.separator.continuation.line.python, source.python
              : source.python
              : source.python
200           : constant.numeric.dec.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
pass          : keyword.control.flow.python, source.python
    case      : keyword.control.flow.python, source.python
              : source.python
(             : punctuation.parenthesis.begin.python, source.python
              : source.python
300           : constant.numeric.dec.python, source.python
              : source.python
)             : punctuation.parenthesis.end.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
pass          : keyword.control.flow.python, source.python
    case      : keyword.control.flow.python, source.python
              : source.python
[             : punctuation.definition.list.begin.python, source.python
              : source.python
400           : constant.numeric.dec.python, source.python
              : source.python
]             : punctuation.definition.list.end.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
pass          : keyword.control.flow.python, source.python
    case      : keyword.control.flow.python, source.python
              : source.python
{             : punctuation.definition.dict.begin.python, source.python
              : source.python
500           : constant.numeric.dec.python, source.python
:             : punctuation.separator.dict.python, source.python
              : source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
,             : punctuation.separator.element.python, source.python
              : source.python
}             : punctuation.definition.dict.end.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
pass          : keyword.control.flow.python, source.python
    case      : keyword.control.flow.python, source.python
              : source.python
Point         : meta.function-call.generic.python, meta.function-call.python, source.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
x             : meta.function-call.arguments.python, meta.function-call.python, source.python
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python
y             : meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
              : source.python
as            : keyword.control.flow.python, source.python
              : source.python
p             : source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
pass          : keyword.control.flow.python, source.python
    case      : keyword.control.flow.python, source.python
              : source.python
600           : constant.numeric.dec.python, source.python
              : source.python
|             : keyword.operator.bitwise.python, source.python
              : source.python
700           : constant.numeric.dec.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
pass          : keyword.control.flow.python, source.python
    case      : keyword.control.flow.python, source.python
              : source.python
_             : source.python
:             : punctuation.separator.colon.python, source.python
