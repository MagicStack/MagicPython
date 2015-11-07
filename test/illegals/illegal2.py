a&&b||c
a &&= a
b ||= c



a             : source.python
&&            : invalid.illegal.operator.python, source.python
b             : source.python
||            : invalid.illegal.operator.python, source.python
c             : source.python
a             : source.python
              : source.python
&&            : invalid.illegal.operator.python, source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
a             : source.python
b             : source.python
              : source.python
||            : invalid.illegal.operator.python, source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
c             : source.python
