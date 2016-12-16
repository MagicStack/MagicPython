try:
    1/0
except AbcError as ex:
    pass
except (ZeroDivisionError, GhiError) as ex:
    print(ex)
else:
    1
finally:
    2



try           : keyword.control.flow.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
1             : constant.numeric.dec.python, source.python
/             : keyword.operator.arithmetic.python, source.python
0             : constant.numeric.dec.python, source.python
except        : keyword.control.flow.python, source.python
              : source.python
AbcError      : source.python
              : source.python
as            : keyword.control.flow.python, source.python
              : source.python
ex            : source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
pass          : keyword.control.flow.python, source.python
except        : keyword.control.flow.python, source.python
              : source.python
(             : punctuation.parenthesis.begin.python, source.python
ZeroDivisionError : source.python, support.type.exception.python
,             : punctuation.separator.element.python, source.python
              : source.python
GhiError      : source.python
)             : punctuation.parenthesis.end.python, source.python
              : source.python
as            : keyword.control.flow.python, source.python
              : source.python
ex            : source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
print         : meta.function-call.python, source.python, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
ex            : meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
else          : keyword.control.flow.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
1             : constant.numeric.dec.python, source.python
finally       : keyword.control.flow.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
2             : constant.numeric.dec.python, source.python
