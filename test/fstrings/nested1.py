f'''
    prefix {
        foo(f"""
            inner prefix
            { bar["q"] + f'insane{42 + 9000}stuff{def aaa(): pass}111'}
            inner suffix
        """)
    } suffix
'''




f             : meta.fstring.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.multi.python
'''           : meta.fstring.python, punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.quoted.multi.python
              : meta.fstring.python, source.python, string.interpolated.python, string.quoted.multi.python
    prefix    : meta.fstring.python, source.python, string.interpolated.python, string.quoted.multi.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
              : meta.fstring.python, source.python
foo           : meta.fstring.python, meta.function-call.generic.python, meta.function-call.python, source.python
(             : meta.fstring.python, meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
f             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.multi.python
"""           : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.quoted.multi.python
              : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python, string.interpolated.python, string.quoted.multi.python
            inner prefix : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python, string.interpolated.python, string.quoted.multi.python
              : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python, string.interpolated.python, string.quoted.multi.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python
              : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python
bar           : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, meta.item-access.python, source.python
[             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, meta.item-access.python, punctuation.definition.arguments.begin.python, source.python
"             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, meta.item-access.arguments.python, meta.item-access.python, punctuation.definition.string.begin.python, source.python, string.quoted.single.python
q             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, meta.item-access.arguments.python, meta.item-access.python, source.python, string.quoted.single.python
"             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, meta.item-access.arguments.python, meta.item-access.python, punctuation.definition.string.end.python, source.python, string.quoted.single.python
]             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, meta.item-access.python, punctuation.definition.arguments.end.python, source.python
              : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python
+             : keyword.operator.arithmetic.python, meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python
              : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python
f             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.single.python
'             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.quoted.single.python
insane        : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python, string.interpolated.python, string.quoted.single.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python
42            : constant.numeric.dec.python, meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python
              : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python
+             : keyword.operator.arithmetic.python, meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python
              : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python
9000          : constant.numeric.dec.python, meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python
stuff         : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python, string.interpolated.python, string.quoted.single.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python
def           : keyword.control.flow.python, meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python
              : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python
aaa           : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.generic.python, meta.function-call.python, source.python
(             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
)             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.arguments.end.python, source.python
:             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.colon.python, source.python
              : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python
pass          : keyword.control.flow.python, meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python
111           : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python, string.interpolated.python, string.quoted.single.python
'             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.single.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python
              : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python, string.interpolated.python, string.quoted.multi.python
            inner suffix : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python, string.interpolated.python, string.quoted.multi.python
              : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.python, string.interpolated.python, string.quoted.multi.python
"""           : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.multi.python
)             : meta.fstring.python, meta.function-call.python, punctuation.definition.arguments.end.python, source.python
              : meta.fstring.python, source.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
 suffix       : meta.fstring.python, source.python, string.interpolated.python, string.quoted.multi.python
'''           : meta.fstring.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.multi.python
