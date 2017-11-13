# this is testing trailing whitespace after the decorator
# DO NOT DELETE TRAILING WHITESTAPCE IN THIS FILE
@foo    
@foo()    
@bar	
@bar()	
@bar() illegal # legal
@bar():   
def baz(): pass





#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 this is testing trailing whitespace after the decorator : comment.line.number-sign.python, source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 DO NOT DELETE TRAILING WHITESTAPCE IN THIS FILE : comment.line.number-sign.python, source.python
@             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.definition.decorator.python, source.python
foo           : entity.name.function.decorator.python, meta.function.decorator.python, source.python
              : meta.function.decorator.python, source.python
@             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.definition.decorator.python, source.python
foo           : entity.name.function.decorator.python, meta.function.decorator.python, source.python
(             : meta.function.decorator.python, punctuation.definition.arguments.begin.python, source.python
)             : meta.function.decorator.python, punctuation.definition.arguments.end.python, source.python
              : source.python
@             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.definition.decorator.python, source.python
bar           : entity.name.function.decorator.python, meta.function.decorator.python, source.python
	             : meta.function.decorator.python, source.python
@             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.definition.decorator.python, source.python
bar           : entity.name.function.decorator.python, meta.function.decorator.python, source.python
(             : meta.function.decorator.python, punctuation.definition.arguments.begin.python, source.python
)             : meta.function.decorator.python, punctuation.definition.arguments.end.python, source.python
	             : source.python
@             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.definition.decorator.python, source.python
bar           : entity.name.function.decorator.python, meta.function.decorator.python, source.python
(             : meta.function.decorator.python, punctuation.definition.arguments.begin.python, source.python
)             : meta.function.decorator.python, punctuation.definition.arguments.end.python, source.python
 illegal      : invalid.illegal.decorator.python, meta.function.decorator.python, source.python
              : source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 legal        : comment.line.number-sign.python, source.python
@             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.definition.decorator.python, source.python
bar           : entity.name.function.decorator.python, meta.function.decorator.python, source.python
(             : meta.function.decorator.python, punctuation.definition.arguments.begin.python, source.python
)             : meta.function.decorator.python, punctuation.definition.arguments.end.python, source.python
:             : invalid.illegal.decorator.python, meta.function.decorator.python, source.python
              : source.python
def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
baz           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
pass          : keyword.control.flow.python, source.python
