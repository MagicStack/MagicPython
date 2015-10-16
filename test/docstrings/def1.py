'TEST'

class Foo:
    'TEST'

    def foo(self, a:'TEST')
                -> 'TEST':
        'TEST'
        with bar:
            pass

    def bar(self, a:'TEST')
                -> 'TEST': pass
        'TEST'
        with bar:
            pass





'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.single.python
TEST          : source.python, string.quoted.single.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.single.python
              : source.python
class         : meta.class.python, source.python, storage.type.class.python
              : meta.class.python, source.python
Foo           : entity.name.type.class.python, meta.class.python, source.python
:             : meta.class.python, punctuation.section.class.begin.python, source.python
              : source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.single.python
TEST          : source.python, string.quoted.single.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.single.python
              : source.python
              : meta.function.python, source.python
def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
self          : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.pyhton
,             : meta.function.parameters.python, meta.function.python, punctuation.separator.parameters.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
a             : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.pyhton
:             : meta.function.parameters.python, meta.function.python, punctuation.separator.annotation.python, source.python
'             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.begin.python, source.python, string.quoted.single.single.python
TEST          : meta.function.parameters.python, meta.function.python, source.python, string.quoted.single.single.python
'             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.end.python, source.python, string.quoted.single.single.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
                 : meta.function.python, source.python
->            : meta.function.python, punctuation.separator.annotation.result.python, source.python
              : meta.function.python, source.python
'             : meta.function.python, punctuation.definition.string.begin.python, source.python, string.quoted.single.single.python
TEST          : meta.function.python, source.python, string.quoted.single.single.python
'             : meta.function.python, punctuation.definition.string.end.python, source.python, string.quoted.single.single.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.single.python
TEST          : source.python, string.quoted.single.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.single.python
              : source.python
with          : keyword.control.flow.python, source.python
 bar:         : source.python
              : source.python
pass          : keyword.control.flow.python, source.python
              : source.python
              : meta.function.python, source.python
def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
bar           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
self          : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.pyhton
,             : meta.function.parameters.python, meta.function.python, punctuation.separator.parameters.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
a             : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.pyhton
:             : meta.function.parameters.python, meta.function.python, punctuation.separator.annotation.python, source.python
'             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.begin.python, source.python, string.quoted.single.single.python
TEST          : meta.function.parameters.python, meta.function.python, source.python, string.quoted.single.single.python
'             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.end.python, source.python, string.quoted.single.single.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
                 : meta.function.python, source.python
->            : meta.function.python, punctuation.separator.annotation.result.python, source.python
              : meta.function.python, source.python
'             : meta.function.python, punctuation.definition.string.begin.python, source.python, string.quoted.single.single.python
TEST          : meta.function.python, source.python, string.quoted.single.single.python
'             : meta.function.python, punctuation.definition.string.end.python, source.python, string.quoted.single.single.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
pass          : keyword.control.flow.python, source.python
              : source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.single.python
TEST          : source.python, string.quoted.single.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.single.python
              : source.python
with          : keyword.control.flow.python, source.python
 bar:         : source.python
              : source.python
pass          : keyword.control.flow.python, source.python
