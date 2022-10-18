match 'prefix' + foo:
    ... # cases
match "prefix" + foo:
    ... # cases
match f'prefix{foo}':
    ... # cases
match f"prefix{foo}":
    ... # cases
match -foo:
    ... # cases
match not foo:
    ... # cases




match         : keyword.control.flow.python, source.python
              : source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
prefix        : source.python, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
              : source.python
+             : keyword.operator.arithmetic.python, source.python
              : source.python
foo           : source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
...           : constant.other.ellipsis.python, source.python
              : source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 cases        : comment.line.number-sign.python, source.python
match         : keyword.control.flow.python, source.python
              : source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
prefix        : source.python, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
              : source.python
+             : keyword.operator.arithmetic.python, source.python
              : source.python
foo           : source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
...           : constant.other.ellipsis.python, source.python
              : source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 cases        : comment.line.number-sign.python, source.python
match         : keyword.control.flow.python, source.python
              : source.python
f             : meta.fstring.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.single.python
'             : meta.fstring.python, punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.quoted.single.python
prefix        : meta.fstring.python, source.python, string.interpolated.python, string.quoted.single.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
foo           : meta.fstring.python, source.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
'             : meta.fstring.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.single.python
:             : punctuation.separator.colon.python, source.python
              : source.python
...           : constant.other.ellipsis.python, source.python
              : source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 cases        : comment.line.number-sign.python, source.python
match         : keyword.control.flow.python, source.python
              : source.python
f             : meta.fstring.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.quoted.single.python
prefix        : meta.fstring.python, source.python, string.interpolated.python, string.quoted.single.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
foo           : meta.fstring.python, source.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
"             : meta.fstring.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.single.python
:             : punctuation.separator.colon.python, source.python
              : source.python
...           : constant.other.ellipsis.python, source.python
              : source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 cases        : comment.line.number-sign.python, source.python
match         : keyword.control.flow.python, source.python
              : source.python
-             : keyword.operator.arithmetic.python, source.python
foo           : source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
...           : constant.other.ellipsis.python, source.python
              : source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 cases        : comment.line.number-sign.python, source.python
match         : keyword.control.flow.python, source.python
              : source.python
not           : keyword.operator.logical.python, source.python
              : source.python
foo           : source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
...           : constant.other.ellipsis.python, source.python
              : source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 cases        : comment.line.number-sign.python, source.python