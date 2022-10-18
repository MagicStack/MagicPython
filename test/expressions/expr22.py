match = 13
case = 12
if case == 4:
  return match * 5



match         : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
13            : constant.numeric.dec.python, source.python
case          : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
12            : constant.numeric.dec.python, source.python
if            : keyword.control.flow.python, source.python
              : source.python
case          : source.python
              : source.python
==            : keyword.operator.comparison.python, source.python
              : source.python
4             : constant.numeric.dec.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
return        : keyword.control.flow.python, source.python
              : source.python
match         : source.python
              : source.python
*             : keyword.operator.arithmetic.python, source.python
              : source.python
5             : constant.numeric.dec.python, source.python
