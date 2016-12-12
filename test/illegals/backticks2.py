a = `\
123`
print a



a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
`             : invalid.deprecated.backtick.python, source.python
\             : invalid.deprecated.backtick.python, punctuation.separator.continuation.line.python, source.python
              : invalid.deprecated.backtick.python, source.python
123           : constant.numeric.dec.python, invalid.deprecated.backtick.python, source.python
`             : invalid.deprecated.backtick.python, source.python
print         : source.python, support.function.builtin.python
              : source.python
a             : source.python
