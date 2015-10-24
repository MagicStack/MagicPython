def foo():
    "TE\"ST"

def foo():
    r"TE\"ST"

def foo():
    R"TE\"ST"

def foo():
    u"TEST"

def foo():
    U"TEST"

def foo():
    b"TEST"

def foo():
    B"TEST"



def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.single.python
TE            : source.python, string.quoted.docstring.single.python
\"            : constant.character.escape.python, source.python, string.quoted.docstring.single.python
ST            : source.python, string.quoted.docstring.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.docstring.single.python
              : source.python
def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
r             : source.python, storage.type.string.python, string.quoted.docstring.raw.single.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.raw.single.python
TE            : source.python, string.quoted.docstring.raw.single.python
\"            : source.python, string.quoted.docstring.raw.single.python
ST            : source.python, string.quoted.docstring.raw.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.docstring.raw.single.python
              : source.python
def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
R             : source.python, storage.type.string.python, string.quoted.docstring.raw.single.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.raw.single.python
TE            : source.python, string.quoted.docstring.raw.single.python
\"            : source.python, string.quoted.docstring.raw.single.python
ST            : source.python, string.quoted.docstring.raw.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.docstring.raw.single.python
              : source.python
def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
u             : source.python, storage.type.string.python, string.quoted.single.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
TEST          : source.python, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
              : source.python
def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
U             : source.python, storage.type.string.python, string.quoted.single.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
TEST          : source.python, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
              : source.python
def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
b             : source.python, storage.type.string.python, string.quoted.binary.single.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.binary.single.python
TEST          : source.python, string.quoted.binary.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.binary.single.python
              : source.python
def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
B             : source.python, storage.type.string.python, string.quoted.binary.single.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.binary.single.python
TEST          : source.python, string.quoted.binary.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.binary.single.python
