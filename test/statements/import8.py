try:
    import \
                    time as ham, \
                    datetime \
            # XXX: comment at the end of import
except Exception as exc:
    pass




try           : keyword.control.flow.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
import        : keyword.control.import.python, source.python
              : source.python
\             : punctuation.separator.continuation.line.python, source.python
              : source.python
                     : source.python
time          : source.python
              : source.python
as            : keyword.control.import.python, source.python
              : source.python
ham           : source.python
,             : punctuation.separator.element.python, source.python
              : source.python
\             : punctuation.separator.continuation.line.python, source.python
              : source.python
                     : source.python
datetime      : source.python
              : source.python
\             : punctuation.separator.continuation.line.python, source.python
              : source.python
              : source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
              : comment.line.number-sign.python, source.python
XXX           : comment.line.number-sign.python, keyword.codetag.notation.python, source.python
: comment at the end of import : comment.line.number-sign.python, source.python
except        : keyword.control.flow.python, source.python
              : source.python
Exception     : source.python, support.type.exception.python
              : source.python
as            : keyword.control.flow.python, source.python
              : source.python
exc           : source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
pass          : keyword.control.flow.python, source.python
