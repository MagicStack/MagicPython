a = '''
{{ before detection }}
{# jinja comment #}
{{ after detection }}
'''



a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.multi.python
{{            : constant.character.format.placeholder.other.python, source.python, string.quoted.multi.python
 before detection  : source.python, string.quoted.multi.python
}}            : constant.character.format.placeholder.other.python, source.python, string.quoted.multi.python
{# jinja comment #} : source.python, string.quoted.multi.python
{{ after detection }} : source.python, string.quoted.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.multi.python
