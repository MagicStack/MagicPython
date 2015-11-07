a = '''\n
{% for item in seq %}
    \n {{ item }} \n \N{BLACK SPADE SUIT}
{% endfor %}
'''



a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.multi.python
\n            : constant.character.escape.python, source.python, string.quoted.multi.python
{% for item in seq %} : source.python, string.quoted.multi.python
              : source.python, string.quoted.multi.python
\n            : constant.character.escape.python, source.python, string.quoted.multi.python
 {{ item }}   : source.python, string.quoted.multi.python
\n            : constant.character.escape.python, source.python, string.quoted.multi.python
              : source.python, string.quoted.multi.python
\N{BLACK SPADE SUIT} : constant.character.escape.python, source.python, string.quoted.multi.python
{% endfor %}  : source.python, string.quoted.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.multi.python
