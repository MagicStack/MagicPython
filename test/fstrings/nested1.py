f'''
    prefix {
        foo(f"""
            inner prefix
            { bar["q"] + f'insane{42 + 9000}stuff{def aaa(): pass}111'}
            inner suffix
        """)
    } suffix
'''




f             : source.python, storage.type.string.python, string.quoted.multi.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.multi.python
              : source.python, string.quoted.multi.python
    prefix    : source.python, string.quoted.multi.python
{             : constant.character.format.placeholder.other.python, source.python
              : source.python
foo           : meta.function-call.generic.python, meta.function-call.python, source.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
f             : meta.function-call.arguments.python, meta.function-call.python, source.python, storage.type.string.python, string.quoted.multi.python
"""           : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.python, string.quoted.multi.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python, string.quoted.multi.python
            inner prefix : meta.function-call.arguments.python, meta.function-call.python, source.python, string.quoted.multi.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python, string.quoted.multi.python
{             : constant.character.format.placeholder.other.python, meta.function-call.arguments.python, meta.function-call.python, source.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python
bar           : meta.function-call.arguments.python, meta.function-call.python, meta.item-access.python, source.python
[             : meta.function-call.arguments.python, meta.function-call.python, meta.item-access.python, punctuation.definition.arguments.begin.python, source.python
"             : meta.function-call.arguments.python, meta.function-call.python, meta.item-access.arguments.python, meta.item-access.python, punctuation.definition.string.begin.python, source.python, string.quoted.single.python
q             : meta.function-call.arguments.python, meta.function-call.python, meta.item-access.arguments.python, meta.item-access.python, source.python, string.quoted.single.python
"             : meta.function-call.arguments.python, meta.function-call.python, meta.item-access.arguments.python, meta.item-access.python, punctuation.definition.string.end.python, source.python, string.quoted.single.python
]             : meta.function-call.arguments.python, meta.function-call.python, meta.item-access.python, punctuation.definition.arguments.end.python, source.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python
+             : keyword.operator.arithmetic.python, meta.function-call.arguments.python, meta.function-call.python, source.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python
f             : meta.function-call.arguments.python, meta.function-call.python, source.python, storage.type.string.python, string.quoted.single.python
'             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.python, string.quoted.single.python
insane        : meta.function-call.arguments.python, meta.function-call.python, source.python, string.quoted.single.python
{             : constant.character.format.placeholder.other.python, meta.function-call.arguments.python, meta.function-call.python, source.python
42            : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, source.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python
+             : keyword.operator.arithmetic.python, meta.function-call.arguments.python, meta.function-call.python, source.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python
9000          : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, source.python
}             : constant.character.format.placeholder.other.python, meta.function-call.arguments.python, meta.function-call.python, source.python
stuff         : meta.function-call.arguments.python, meta.function-call.python, source.python, string.quoted.single.python
{             : constant.character.format.placeholder.other.python, meta.function-call.arguments.python, meta.function-call.python, source.python
def           : keyword.control.flow.python, meta.function-call.arguments.python, meta.function-call.python, source.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python
aaa           : meta.function-call.arguments.python, meta.function-call.generic.python, meta.function-call.python, source.python
(             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
)             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.arguments.end.python, source.python
:             : meta.function-call.arguments.python, meta.function-call.python, source.python
pass          : keyword.control.flow.python, meta.function-call.arguments.python, meta.function-call.python, source.python
}             : constant.character.format.placeholder.other.python, meta.function-call.arguments.python, meta.function-call.python, source.python
111           : meta.function-call.arguments.python, meta.function-call.python, source.python, string.quoted.single.python
'             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.python, string.quoted.single.python
}             : constant.character.format.placeholder.other.python, meta.function-call.arguments.python, meta.function-call.python, source.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python, string.quoted.multi.python
            inner suffix : meta.function-call.arguments.python, meta.function-call.python, source.python, string.quoted.multi.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python, string.quoted.multi.python
"""           : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.python, string.quoted.multi.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
              : source.python
}             : constant.character.format.placeholder.other.python, source.python
 suffix       : source.python, string.quoted.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.multi.python
