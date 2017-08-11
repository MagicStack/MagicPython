a = f"normal {{ normal }} normal } {10!r} normal {fo.__add__!s}"



a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
f             : meta.fstring.python, source.python, storage.type.string.python, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, punctuation.definition.string.begin.python, source.python, string.interpolated.python, string.quoted.single.python
normal        : meta.fstring.python, source.python, string.interpolated.python, string.quoted.single.python
{{            : constant.character.escape.python, meta.fstring.python, source.python
 normal       : meta.fstring.python, source.python, string.interpolated.python, string.quoted.single.python
}}            : constant.character.escape.python, meta.fstring.python, source.python
 normal       : meta.fstring.python, source.python, string.interpolated.python, string.quoted.single.python
}             : invalid.illegal.brace.python, meta.fstring.python, source.python
              : meta.fstring.python, source.python, string.interpolated.python, string.quoted.single.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
10            : constant.numeric.dec.python, meta.fstring.python, source.python
!r            : meta.fstring.python, source.python, storage.type.format.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
 normal       : meta.fstring.python, source.python, string.interpolated.python, string.quoted.single.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
fo            : meta.fstring.python, source.python
.             : meta.fstring.python, punctuation.separator.period.python, source.python
__add__       : meta.fstring.python, source.python, support.function.magic.python
!s            : meta.fstring.python, source.python, storage.type.format.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.python
"             : meta.fstring.python, punctuation.definition.string.end.python, source.python, string.interpolated.python, string.quoted.single.python
