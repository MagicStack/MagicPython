# XXX we have to highlight '% o' here, as it is a valid python
# format spec. Otherwise, it would be hard to spot an error in
# the code below.
a = '12% of %s' % ('name',)



#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
              : comment.line.number-sign.python, source.python
XXX           : comment.line.number-sign.python, keyword.codetag.notation.python, source.python
 we have to highlight '% o' here, as it is a valid python : comment.line.number-sign.python, source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 format spec. Otherwise, it would be hard to spot an error in : comment.line.number-sign.python, source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 the code below. : comment.line.number-sign.python, source.python
a             : source.python
              : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
12            : source.python, string.quoted.single.python
% o           : constant.character.format.placeholder.other.python, source.python, string.quoted.single.python
f             : source.python, string.quoted.single.python
%s            : constant.character.format.placeholder.other.python, source.python, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
              : source.python
%             : keyword.operator.arithmetic.python, source.python
              : source.python
(             : punctuation.parenthesis.begin.python, source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
name          : source.python, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
,             : punctuation.separator.element.python, source.python
)             : punctuation.parenthesis.end.python, source.python
