a[1] = b'''
multiline 'binary' string \

    \xf1 \u1234aaaa \U1234aaaa

    \N{BLACK SPADE SUIT}
'''



a             : meta.item-access.python, source.python
[             : meta.function-call.arguments.python, meta.item-access.python, punctuation.definition.arguments.begin.python, source.python
1             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.item-access.arguments.python, meta.item-access.python, source.python
]             : meta.item-access.python, punctuation.definition.arguments.end.python, source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
b             : source.python, storage.type.string.python, string.quoted.multi.binary.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.multi.binary.python
multiline 'binary' string  : source.python, string.quoted.multi.binary.python
\             : constant.language.python, source.python, string.quoted.multi.binary.python
              : source.python, string.quoted.multi.binary.python
              : source.python, string.quoted.multi.binary.python
\xf1          : constant.character.python, source.python, string.quoted.multi.binary.python
 \u1234aaaa \U1234aaaa : source.python, string.quoted.multi.binary.python
              : source.python, string.quoted.multi.binary.python
    \N{BLACK SPADE SUIT} : source.python, string.quoted.multi.binary.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.multi.binary.python
