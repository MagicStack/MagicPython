from ... import foo as bar
raise Exception('done') from exc
yield from foo




from          : keyword.control.import.python, source.python
              : source.python
...           : punctuation.separator.period.python, source.python
              : source.python
import        : keyword.control.import.python, source.python
              : source.python
foo           : source.python
              : source.python
as            : keyword.control.import.python, source.python
              : source.python
bar           : source.python
raise         : keyword.control.flow.python, source.python
              : source.python
Exception     : meta.function-call.python, source.python, support.type.exception.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
'             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.python, string.quoted.single.python
done          : meta.function-call.arguments.python, meta.function-call.python, source.python, string.quoted.single.python
'             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.python, string.quoted.single.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
              : source.python
from          : keyword.control.flow.python, source.python
              : source.python
exc           : source.python
yield from    : keyword.control.flow.python, source.python
              : source.python
foo           : source.python
