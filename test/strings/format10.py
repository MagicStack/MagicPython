a = '''blah {foo-bar %d
       blah {foo-bar %d}
       blah {foo-bar %d //insane {}}
       {}blah {foo-bar %d //insane {}}'''



a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.multi.python
blah {foo-bar  : source.python, string.quoted.multi.python
%d            : constant.character.format.placeholder.other.python, source.python, string.quoted.multi.python
       blah   : source.python, string.quoted.multi.python
{foo-bar      : source.python, string.quoted.multi.python
%d            : constant.character.format.placeholder.other.python, source.python, string.quoted.multi.python
}             : source.python, string.quoted.multi.python
       blah {foo-bar  : source.python, string.quoted.multi.python
%d            : constant.character.format.placeholder.other.python, source.python, string.quoted.multi.python
 //insane {}} : source.python, string.quoted.multi.python
       {}blah {foo-bar  : source.python, string.quoted.multi.python
%d            : constant.character.format.placeholder.other.python, source.python, string.quoted.multi.python
 //insane {}} : source.python, string.quoted.multi.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.multi.python
