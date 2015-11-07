a = "simple \\ string \
foo \' \" \a \b \c \f \n \r \t \v \5 \55 \555 \05 \005"



a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
simple        : source.python, string.quoted.single.python
\\            : constant.character.escape.python, source.python, string.quoted.single.python
 string       : source.python, string.quoted.single.python
\             : constant.language.python, source.python, string.quoted.single.python
foo           : source.python, string.quoted.single.python
\'            : constant.character.escape.python, source.python, string.quoted.single.python
              : source.python, string.quoted.single.python
\"            : constant.character.escape.python, source.python, string.quoted.single.python
              : source.python, string.quoted.single.python
\a            : constant.character.escape.python, source.python, string.quoted.single.python
              : source.python, string.quoted.single.python
\b            : constant.character.escape.python, source.python, string.quoted.single.python
 \c           : source.python, string.quoted.single.python
\f            : constant.character.escape.python, source.python, string.quoted.single.python
              : source.python, string.quoted.single.python
\n            : constant.character.escape.python, source.python, string.quoted.single.python
              : source.python, string.quoted.single.python
\r            : constant.character.escape.python, source.python, string.quoted.single.python
              : source.python, string.quoted.single.python
\t            : constant.character.escape.python, source.python, string.quoted.single.python
              : source.python, string.quoted.single.python
\v            : constant.character.escape.python, source.python, string.quoted.single.python
              : source.python, string.quoted.single.python
\5            : constant.character.escape.python, source.python, string.quoted.single.python
              : source.python, string.quoted.single.python
\55           : constant.character.escape.python, source.python, string.quoted.single.python
              : source.python, string.quoted.single.python
\555          : constant.character.escape.python, source.python, string.quoted.single.python
              : source.python, string.quoted.single.python
\05           : constant.character.escape.python, source.python, string.quoted.single.python
              : source.python, string.quoted.single.python
\005          : constant.character.escape.python, source.python, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
