from.foo import d
from.import a

foo.import

raise Exception from Foo

def bar():
    yield from baz



from          : keyword.control.import.python, source.python
.             : punctuation.separator.period.python, source.python
foo           : source.python
              : source.python
import        : keyword.control.import.python, source.python
              : source.python
d             : source.python
from          : keyword.control.import.python, source.python
.             : punctuation.separator.period.python, source.python
import        : keyword.control.import.python, source.python
              : source.python
a             : source.python
              : source.python
foo           : source.python
.             : punctuation.separator.period.python, source.python
import        : keyword.control.import.python, source.python
              : source.python
raise         : keyword.control.flow.python, source.python
              : source.python
Exception     : source.python, support.type.exception.python
              : source.python
from          : keyword.control.flow.python, source.python
              : source.python
Foo           : source.python
              : source.python
def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
bar           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
yield from    : keyword.control.flow.python, source.python
              : source.python
baz           : source.python
