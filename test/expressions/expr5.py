a = (from, a)
b = [from, b]
c = {from: {import: a}}



a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
(             : source.python
from          : keyword.control.flow.python, source.python
, a           : source.python
)             : source.python
b             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
[             : source.python
from          : keyword.control.flow.python, source.python
, b           : source.python
]             : source.python
c             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
{             : source.python
from          : keyword.control.flow.python, source.python
:             : source.python
{             : source.python
import        : keyword.control.flow.python, source.python
: a           : source.python
}             : source.python
}             : source.python
