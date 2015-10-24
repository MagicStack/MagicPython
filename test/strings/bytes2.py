a[1] = b'''
multiline 'binary' string \

    \xf1 \u1234aaaa \U1234aaaa

    \N{BLACK SPADE SUIT}
'''



a             : meta.item-access.python, source.python
[             : meta.item-access.python, punctuation.definition.arguments.begin.python, source.python
1             : constant.numeric.dec.python, meta.item-access.arguments.python, meta.item-access.python, source.python
]             : meta.item-access.python, punctuation.definition.arguments.end.python, source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
b             : source.python, storage.type.string.python, string.quoted.binary.multi.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.binary.multi.python
multiline 'binary' string  : source.python, string.quoted.binary.multi.python
\             : constant.language.python, source.python, string.quoted.binary.multi.python
              : source.python, string.quoted.binary.multi.python
              : source.python, string.quoted.binary.multi.python
\xf1          : constant.character.escape.python, source.python, string.quoted.binary.multi.python
 \u1234aaaa \U1234aaaa : source.python, string.quoted.binary.multi.python
              : source.python, string.quoted.binary.multi.python
    \N{BLACK SPADE SUIT} : source.python, string.quoted.binary.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.binary.multi.python
