f'abc \} }} }}} }}}} }}}}} efg'




f             : source.python, storage.type.string.python, string.quoted.single.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
abc           : source.python, string.quoted.single.python
\             : source.python, string.quoted.single.python
}             : invalid.illegal.brace.python, source.python
              : source.python, string.quoted.single.python
}}            : constant.character.escape.python, source.python
              : source.python, string.quoted.single.python
}}            : constant.character.escape.python, source.python
}             : invalid.illegal.brace.python, source.python
              : source.python, string.quoted.single.python
}}            : constant.character.escape.python, source.python
}}            : constant.character.escape.python, source.python
              : source.python, string.quoted.single.python
}}            : constant.character.escape.python, source.python
}}            : constant.character.escape.python, source.python
}             : invalid.illegal.brace.python, source.python
 efg          : source.python, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
