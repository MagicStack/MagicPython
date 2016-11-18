a = f"normal \{ normal \} normal {10!r} normal {fo.__add__!s}"



a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
f             : source.python, storage.type.string.python, string.quoted.single.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
normal        : source.python, string.quoted.single.python
\{            : constant.character.escape.python, source.python
 normal       : source.python, string.quoted.single.python
\}            : constant.character.escape.python, source.python
 normal       : source.python, string.quoted.single.python
{             : constant.character.format.placeholder.other.python, source.python
10            : constant.numeric.dec.python, source.python
!r            : source.python, storage.type.format.python
}             : constant.character.format.placeholder.other.python, source.python
 normal       : source.python, string.quoted.single.python
{             : constant.character.format.placeholder.other.python, source.python
fo            : source.python
.             : source.python
__add__       : source.python, support.function.magic.python
!s            : source.python, storage.type.format.python
}             : constant.character.format.placeholder.other.python, source.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
