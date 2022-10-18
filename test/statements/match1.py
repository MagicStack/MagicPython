def foo(status):
    match status:
        case 404:
            return "Not found"
        case 401 | 403:
            return "Not allowed"
        case _:
            return "Something's wrong with the internet"




def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
status        : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
match         : keyword.control.flow.python, source.python
              : source.python
status        : source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
case          : keyword.control.flow.python, source.python
              : source.python
404           : constant.numeric.dec.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
return        : keyword.control.flow.python, source.python
              : source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
Not found     : source.python, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
              : source.python
case          : keyword.control.flow.python, source.python
              : source.python
401           : constant.numeric.dec.python, source.python
              : source.python
|             : keyword.operator.bitwise.python, source.python
              : source.python
403           : constant.numeric.dec.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
return        : keyword.control.flow.python, source.python
              : source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
Not allowed   : source.python, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
              : source.python
case          : keyword.control.flow.python, source.python
              : source.python
_             : source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
return        : keyword.control.flow.python, source.python
              : source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
Something's wrong with the internet : source.python, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
