r'''Module docstring

    simple \\ string \
    foo \' \" \a \b \c \f \n \r \t \v \5 \55 \555 \05 \005

    multiline "unicode" string \
    \xf1 \u1234aaaa \U1234aaaa
    \N{BLACK SPADE SUIT}
'''



r             : source.python, storage.type.string.python, string.quoted.docstring.raw.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.raw.python
Module docstring : source.python, string.quoted.docstring.raw.python
              : source.python, string.quoted.docstring.raw.python
    simple    : source.python, string.quoted.docstring.raw.python
\\            : constant.character.python, source.python, string.quoted.docstring.raw.python
 string       : source.python, string.quoted.docstring.raw.python
\             : constant.language.python, source.python, string.quoted.docstring.raw.python
    foo       : source.python, string.quoted.docstring.raw.python
\'            : constant.character.python, source.python, string.quoted.docstring.raw.python
              : source.python, string.quoted.docstring.raw.python
\"            : constant.character.python, source.python, string.quoted.docstring.raw.python
              : source.python, string.quoted.docstring.raw.python
\a            : constant.character.python, source.python, string.quoted.docstring.raw.python
              : source.python, string.quoted.docstring.raw.python
\b            : constant.character.python, source.python, string.quoted.docstring.raw.python
 \c           : source.python, string.quoted.docstring.raw.python
\f            : constant.character.python, source.python, string.quoted.docstring.raw.python
              : source.python, string.quoted.docstring.raw.python
\n            : constant.character.python, source.python, string.quoted.docstring.raw.python
              : source.python, string.quoted.docstring.raw.python
\r            : constant.character.python, source.python, string.quoted.docstring.raw.python
              : source.python, string.quoted.docstring.raw.python
\t            : constant.character.python, source.python, string.quoted.docstring.raw.python
              : source.python, string.quoted.docstring.raw.python
\v            : constant.character.python, source.python, string.quoted.docstring.raw.python
              : source.python, string.quoted.docstring.raw.python
\5            : constant.character.python, source.python, string.quoted.docstring.raw.python
              : source.python, string.quoted.docstring.raw.python
\55           : constant.character.python, source.python, string.quoted.docstring.raw.python
              : source.python, string.quoted.docstring.raw.python
\555          : constant.character.python, source.python, string.quoted.docstring.raw.python
              : source.python, string.quoted.docstring.raw.python
\05           : constant.character.python, source.python, string.quoted.docstring.raw.python
              : source.python, string.quoted.docstring.raw.python
\005          : constant.character.python, source.python, string.quoted.docstring.raw.python
              : source.python, string.quoted.docstring.raw.python
    multiline "unicode" string  : source.python, string.quoted.docstring.raw.python
\             : constant.language.python, source.python, string.quoted.docstring.raw.python
              : source.python, string.quoted.docstring.raw.python
\xf1          : constant.character.python, source.python, string.quoted.docstring.raw.python
 \u1234aaaa \U1234aaaa : source.python, string.quoted.docstring.raw.python
    \N{BLACK SPADE SUIT} : source.python, string.quoted.docstring.raw.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.docstring.raw.python
