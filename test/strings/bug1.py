# issue 150
record = {
    "a": {k: str(v) for k, v in foo if ""}
}




#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 issue 150    : comment.line.number-sign.python, source.python
record        : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
{             : punctuation.definition.dict.begin.python, source.python
              : source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
a             : source.python, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
:             : punctuation.separator.dict.python, source.python
              : source.python
{             : punctuation.definition.dict.begin.python, source.python
k             : source.python
:             : punctuation.separator.dict.python, source.python
              : source.python
str           : meta.function-call.python, source.python, support.type.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
v             : meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
              : source.python
for           : keyword.control.flow.python, source.python
              : source.python
k             : source.python
,             : punctuation.separator.element.python, source.python
              : source.python
v             : source.python
              : source.python
in            : keyword.operator.logical.python, source.python
              : source.python
foo           : source.python
              : source.python
if            : keyword.control.flow.python, source.python
              : source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
}             : punctuation.definition.dict.end.python, source.python
}             : punctuation.definition.dict.end.python, source.python
