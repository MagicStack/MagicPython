from . . . foo import \
    (
        # XXX: legal comment inside import
        time as bar,
        # another comment
        baz,
        datetime as ham
    )
raise Exception('!') from None




from          : keyword.control.import.python, source.python
              : source.python
.             : punctuation.separator.period.python, source.python
              : source.python
.             : punctuation.separator.period.python, source.python
              : source.python
.             : punctuation.separator.period.python, source.python
              : source.python
foo           : source.python
              : source.python
import        : keyword.control.import.python, source.python
              : source.python
\             : punctuation.separator.continuation.line.python, source.python
              : source.python
              : source.python
(             : punctuation.parenthesis.begin.python, source.python
              : source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
              : comment.line.number-sign.python, source.python
XXX           : comment.line.number-sign.python, keyword.codetag.notation.python, source.python
: legal comment inside import : comment.line.number-sign.python, source.python
              : source.python
time          : source.python
              : source.python
as            : keyword.control.import.python, source.python
              : source.python
bar           : source.python
,             : punctuation.separator.element.python, source.python
              : source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 another comment : comment.line.number-sign.python, source.python
              : source.python
baz           : source.python
,             : punctuation.separator.element.python, source.python
              : source.python
datetime      : source.python
              : source.python
as            : keyword.control.import.python, source.python
              : source.python
ham           : source.python
              : source.python
)             : punctuation.parenthesis.end.python, source.python
raise         : keyword.control.flow.python, source.python
              : source.python
Exception     : meta.function-call.python, source.python, support.type.exception.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
'             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.python, string.quoted.single.python
!             : meta.function-call.arguments.python, meta.function-call.python, source.python, string.quoted.single.python
'             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.python, string.quoted.single.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
              : source.python
from          : keyword.control.flow.python, source.python
              : source.python
None          : constant.language.python, source.python
