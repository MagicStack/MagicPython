a = '%i' % 42
a = "%(language)s has %(number)03d quote types."
a = b"%(language)s has %(number)03d quote types."
a = R"%(language)s has %(number)03d quote types."



a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
%i            : constant.character.format.placeholder.other.python, meta.format.percent.python, source.python, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
              : source.python
%             : keyword.operator.arithmetic.python, source.python
              : source.python
42            : constant.numeric.dec.python, source.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
%(language)s  : constant.character.format.placeholder.other.python, meta.format.percent.python, source.python, string.quoted.single.python
 has          : source.python, string.quoted.single.python
%(number)03d  : constant.character.format.placeholder.other.python, meta.format.percent.python, source.python, string.quoted.single.python
 quote types. : source.python, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
b             : source.python, storage.type.string.python, string.quoted.binary.single.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.binary.single.python
%(language)s  : constant.character.format.placeholder.other.python, meta.format.percent.python, source.python, string.quoted.binary.single.python
 has          : source.python, string.quoted.binary.single.python
%(number)03d  : constant.character.format.placeholder.other.python, meta.format.percent.python, source.python, string.quoted.binary.single.python
 quote types. : source.python, string.quoted.binary.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.binary.single.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
R             : source.python, storage.type.string.python, string.quoted.raw.single.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.raw.single.python
%(language)s  : constant.character.format.placeholder.other.python, meta.format.percent.python, source.python, string.quoted.raw.single.python
 has          : source.python, string.quoted.raw.single.python
%(number)03d  : constant.character.format.placeholder.other.python, meta.format.percent.python, source.python, string.quoted.raw.single.python
 quote types. : source.python, string.quoted.raw.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.raw.single.python
