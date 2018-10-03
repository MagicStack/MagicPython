# issue 150
cmd = "git-clang-format --style=\"{{BasedOnStyle: Google, ColumnLimit: 100, IndentWidth: 2, " \
 "AlignConsecutiveAssignments: true}}\" {COMMIT_SHA} -- ./**/*.proto > {OUTPUT}".format(




#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 issue 150    : comment.line.number-sign.python, source.python
cmd           : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
git-clang-format --style= : source.python, string.quoted.single.python
\"            : constant.character.escape.python, source.python, string.quoted.single.python
{{            : constant.character.format.placeholder.other.python, meta.format.brace.python, source.python, string.quoted.single.python
BasedOnStyle: Google, ColumnLimit: 100, IndentWidth: 2,  : source.python, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
              : source.python
\             : punctuation.separator.continuation.line.python, source.python
              : source.python
              : source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
AlignConsecutiveAssignments: true : source.python, string.quoted.single.python
}}            : constant.character.format.placeholder.other.python, meta.format.brace.python, source.python, string.quoted.single.python
\"            : constant.character.escape.python, source.python, string.quoted.single.python
              : source.python, string.quoted.single.python
{COMMIT_SHA}  : constant.character.format.placeholder.other.python, meta.format.brace.python, source.python, string.quoted.single.python
 -- ./**/*.proto >  : source.python, string.quoted.single.python
{OUTPUT}      : constant.character.format.placeholder.other.python, meta.format.brace.python, source.python, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
.             : punctuation.separator.period.python, source.python
format        : meta.function-call.generic.python, meta.function-call.python, source.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
