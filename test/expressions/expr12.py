print []
print {}
print 1



print         : meta.item-access.python, source.python, support.function.builtin.python
              : meta.item-access.python, source.python
[             : meta.item-access.python, punctuation.definition.arguments.begin.python, source.python
]             : meta.item-access.python, punctuation.definition.arguments.end.python, source.python
print         : source.python, support.function.builtin.python
              : source.python
{             : punctuation.definition.dict.begin.python, source.python
}             : punctuation.definition.dict.end.python, source.python
print         : source.python, support.function.builtin.python
              : source.python
1             : constant.numeric.dec.python, source.python
