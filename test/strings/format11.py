a = R'''\fr{still_ok}ac{m_{j \rightarrow i}(\mathrm{good})}
        {not_ok} %d
'''



a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
R             : source.python, storage.type.string.python, string.quoted.raw.multi.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.raw.multi.python
\fr           : source.python, string.quoted.raw.multi.python
{still_ok}    : constant.character.format.placeholder.other.python, meta.format.brace.python, source.python, string.quoted.raw.multi.python
ac            : source.python, string.quoted.raw.multi.python
{m_{j \rightarrow i}(\mathrm{good})} : source.python, string.quoted.raw.multi.python
        {not_ok}  : source.python, string.quoted.raw.multi.python
%d            : constant.character.format.placeholder.other.python, meta.format.percent.python, source.python, string.quoted.raw.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.raw.multi.python
