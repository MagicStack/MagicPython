# testing annotations split over multiple lines
def some_func(a:
                 lambda x=None:
                    {key: val
                        for key, val in
                            (x if x is not None else [])
                    }=42):




#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 testing annotations split over multiple lines : comment.line.number-sign.python, source.python
def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
some_func     : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
a             : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.python
:             : meta.function.parameters.python, meta.function.python, punctuation.separator.annotation.python, source.python
                  : meta.function.parameters.python, meta.function.python, source.python
lambda        : meta.function.parameters.python, meta.function.python, meta.lambda-function.python, source.python, storage.type.function.lambda.python
              : meta.function.lambda.parameters.python, meta.function.parameters.python, meta.function.python, meta.lambda-function.python, source.python
x             : meta.function.lambda.parameters.python, meta.function.parameters.python, meta.function.python, meta.lambda-function.python, source.python, variable.parameter.function.language.python
=             : keyword.operator.python, meta.function.lambda.parameters.python, meta.function.parameters.python, meta.function.python, meta.lambda-function.python, source.python
None          : constant.language.python, meta.function.lambda.parameters.python, meta.function.parameters.python, meta.function.python, meta.lambda-function.python, source.python
:             : meta.function.parameters.python, meta.function.python, meta.lambda-function.python, punctuation.section.function.lambda.begin.python, source.python
                     : meta.function.parameters.python, meta.function.python, source.python
{             : meta.function.parameters.python, meta.function.python, punctuation.definition.dict.begin.python, source.python
key           : meta.function.parameters.python, meta.function.python, source.python
:             : meta.function.parameters.python, meta.function.python, punctuation.separator.dict.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
val           : meta.function.parameters.python, meta.function.python, source.python
                         : meta.function.parameters.python, meta.function.python, source.python
for           : keyword.control.flow.python, meta.function.parameters.python, meta.function.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
key           : meta.function.parameters.python, meta.function.python, source.python
,             : meta.function.parameters.python, meta.function.python, punctuation.separator.element.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
val           : meta.function.parameters.python, meta.function.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
in            : keyword.operator.logical.python, meta.function.parameters.python, meta.function.python, source.python
                             : meta.function.parameters.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.parenthesis.begin.python, source.python
x             : meta.function.parameters.python, meta.function.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
if            : keyword.control.flow.python, meta.function.parameters.python, meta.function.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
x             : meta.function.parameters.python, meta.function.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
is            : keyword.operator.logical.python, meta.function.parameters.python, meta.function.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
not           : keyword.operator.logical.python, meta.function.parameters.python, meta.function.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
None          : constant.language.python, meta.function.parameters.python, meta.function.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
else          : keyword.control.flow.python, meta.function.parameters.python, meta.function.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
[             : meta.function.parameters.python, meta.function.python, punctuation.definition.list.begin.python, source.python
]             : meta.function.parameters.python, meta.function.python, punctuation.definition.list.end.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.parenthesis.end.python, source.python
                     : meta.function.parameters.python, meta.function.python, source.python
}             : meta.function.parameters.python, meta.function.python, punctuation.definition.dict.end.python, source.python
=             : keyword.operator.assignment.python, meta.function.parameters.python, meta.function.python, source.python
42            : constant.numeric.dec.python, meta.function.parameters.python, meta.function.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
