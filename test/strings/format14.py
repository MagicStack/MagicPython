a = R'''\n
{% for item in seq %}
    \n {{ item }} \n \N{BLACK SPADE SUIT}
{% endfor %}
'''



a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
R             : source.python, storage.type.string.python, string.quoted.raw.multi.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.raw.multi.python
\n            : source.python, string.quoted.raw.multi.python
{% for item in seq %} : source.python, string.quoted.raw.multi.python
    \n {{ item }} \n \N{BLACK SPADE SUIT} : source.python, string.quoted.raw.multi.python
{% endfor %}  : source.python, string.quoted.raw.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.raw.multi.python
