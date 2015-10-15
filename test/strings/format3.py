'%i' % 42
"%(language)s has %(number)03d quote types."
b"%(language)s has %(number)03d quote types."
R"%(language)s has %(number)03d quote types."



'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.single.python
%i            : constant.character.format.python, source.python, string.quoted.single.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.single.python
              : source.python
%             : keyword.operator.python, source.python
              : source.python
42            : constant.numeric.dec.python, source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.double.single.python
%(language)s  : constant.character.format.python, source.python, string.quoted.double.single.python
 has          : source.python, string.quoted.double.single.python
%(number)03d  : constant.character.format.python, source.python, string.quoted.double.single.python
 quote types. : source.python, string.quoted.double.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.double.single.python
b             : source.python, storage.type.string.python, string.quoted.double.single.binary.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.double.single.binary.python
%(language)s  : constant.character.format.python, source.python, string.quoted.double.single.binary.python
 has          : source.python, string.quoted.double.single.binary.python
%(number)03d  : constant.character.format.python, source.python, string.quoted.double.single.binary.python
 quote types. : source.python, string.quoted.double.single.binary.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.double.single.binary.python
R             : source.python, storage.type.string.python, string.quoted.double.single.raw.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.double.single.raw.python
%(language)s  : constant.character.format.python, source.python, string.quoted.double.single.raw.python
 has          : source.python, string.quoted.double.single.raw.python
%(number)03d  : constant.character.format.python, source.python, string.quoted.double.single.raw.python
 quote types. : source.python, string.quoted.double.single.raw.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.double.single.raw.python
