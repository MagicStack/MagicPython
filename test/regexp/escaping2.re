start\A\b\B\d\D\s\S\w\W\Z\\\1\01\1111\0011\xfab\u123fb\U1234aaaab\c



start         : source.regexp.python
\A            : source.regexp.python, support.other.escape.special.regexp
\b            : source.regexp.python, support.other.escape.special.regexp
\B            : source.regexp.python, support.other.escape.special.regexp
\d            : source.regexp.python, support.other.escape.special.regexp
\D            : source.regexp.python, support.other.escape.special.regexp
\s            : source.regexp.python, support.other.escape.special.regexp
\S            : source.regexp.python, support.other.escape.special.regexp
\w            : source.regexp.python, support.other.escape.special.regexp
\W            : source.regexp.python, support.other.escape.special.regexp
\Z            : source.regexp.python, support.other.escape.special.regexp
\\            : constant.character.escape.regexp, source.regexp.python
\1            : entity.name.tag.backreference.regexp, meta.backreference.regexp, source.regexp.python
\01           : constant.character.escape.regexp, source.regexp.python
\111          : constant.character.escape.regexp, source.regexp.python
1             : source.regexp.python
\001          : constant.character.escape.regexp, source.regexp.python
1             : source.regexp.python
\xfa          : constant.character.escape.regexp, source.regexp.python
b             : source.regexp.python
\u123f        : constant.character.unicode.regexp, source.regexp.python
b             : source.regexp.python
\U1234aaaa    : constant.character.unicode.regexp, source.regexp.python
b             : source.regexp.python
\c            : constant.character.escape.regexp, source.regexp.python
