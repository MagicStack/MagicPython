print "is", 2*2
print("is", 2*2)
print x,
print(x, end=" ")
print
print()
print >>sys.stderr, "er"
print("er", file=sys.stderr)
print (x, y)
print((x, y))



print         : source.python, support.function.builtin.python
              : source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
is            : source.python, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
,             : punctuation.separator.element.python, source.python
              : source.python
2             : constant.numeric.dec.python, source.python
*             : keyword.operator.arithmetic.python, source.python
2             : constant.numeric.dec.python, source.python
print         : meta.function-call.python, source.python, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.python, string.quoted.single.python
is            : meta.function-call.arguments.python, meta.function-call.python, source.python, string.quoted.single.python
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.python, string.quoted.single.python
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python
2             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, source.python
*             : keyword.operator.arithmetic.python, meta.function-call.arguments.python, meta.function-call.python, source.python
2             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
print         : source.python, support.function.builtin.python
              : source.python
x             : source.python
,             : punctuation.separator.element.python, source.python
print         : meta.function-call.python, source.python, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
x             : meta.function-call.arguments.python, meta.function-call.python, source.python
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python
end           : meta.function-call.arguments.python, meta.function-call.python, source.python, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, source.python
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.python, string.quoted.single.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python, string.quoted.single.python
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.python, string.quoted.single.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
print         : source.python, support.function.builtin.python
print         : meta.function-call.python, source.python, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
print         : source.python, support.function.builtin.python
              : source.python
>>            : keyword.operator.bitwise.python, source.python
sys           : source.python
.             : punctuation.separator.period.python, source.python
stderr        : source.python
,             : punctuation.separator.element.python, source.python
              : source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
er            : source.python, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
print         : meta.function-call.python, source.python, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.python, string.quoted.single.python
er            : meta.function-call.arguments.python, meta.function-call.python, source.python, string.quoted.single.python
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.python, string.quoted.single.python
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python
file          : meta.function-call.arguments.python, meta.function-call.python, source.python, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, source.python
sys           : meta.function-call.arguments.python, meta.function-call.python, source.python
.             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.period.python, source.python
stderr        : meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
print         : meta.function-call.python, source.python, support.function.builtin.python
              : meta.function-call.python, source.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
x             : meta.function-call.arguments.python, meta.function-call.python, source.python
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python
y             : meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
print         : meta.function-call.python, source.python, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
(             : meta.function-call.arguments.python, meta.function-call.python, punctuation.parenthesis.begin.python, source.python
x             : meta.function-call.arguments.python, meta.function-call.python, source.python
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.element.python, source.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python
y             : meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.arguments.python, meta.function-call.python, punctuation.parenthesis.end.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
