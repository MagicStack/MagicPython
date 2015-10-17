a = "simple \\ string \
foo \' \" \a \b \c \f \n \r \t \v \5 \55 \555 \05 \005"



a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
simple        : source.python, string.quoted.single.python
\\            : constant.character.python, source.python, string.quoted.single.python
 string       : source.python, string.quoted.single.python
\             : constant.language.python, source.python, string.quoted.single.python
foo           : source.python, string.quoted.single.python
\'            : constant.character.python, source.python, string.quoted.single.python
              : source.python, string.quoted.single.python
\"            : constant.character.python, source.python, string.quoted.single.python
              : source.python, string.quoted.single.python
\a            : constant.character.python, source.python, string.quoted.single.python
              : source.python, string.quoted.single.python
\b            : constant.character.python, source.python, string.quoted.single.python
 \c           : source.python, string.quoted.single.python
\f            : constant.character.python, source.python, string.quoted.single.python
              : source.python, string.quoted.single.python
\n            : constant.character.python, source.python, string.quoted.single.python
              : source.python, string.quoted.single.python
\r            : constant.character.python, source.python, string.quoted.single.python
              : source.python, string.quoted.single.python
\t            : constant.character.python, source.python, string.quoted.single.python
              : source.python, string.quoted.single.python
\v            : constant.character.python, source.python, string.quoted.single.python
              : source.python, string.quoted.single.python
\5            : constant.character.python, source.python, string.quoted.single.python
              : source.python, string.quoted.single.python
\55           : constant.character.python, source.python, string.quoted.single.python
              : source.python, string.quoted.single.python
\555          : constant.character.python, source.python, string.quoted.single.python
              : source.python, string.quoted.single.python
\05           : constant.character.python, source.python, string.quoted.single.python
              : source.python, string.quoted.single.python
\005          : constant.character.python, source.python, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
