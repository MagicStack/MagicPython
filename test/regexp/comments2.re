(?x)
    foo     (?#
comment 1
            ) bar
    baz     (?#comment 2)



(?x)          : source.regexp.python, storage.modifier.flag.regexp
    foo       : source.regexp.python
(?#           : comment.regexp, punctuation.comment.begin.regexp, source.regexp.python
comment 1     : comment.regexp, source.regexp.python
              : comment.regexp, source.regexp.python
)             : comment.regexp, punctuation.comment.end.regexp, source.regexp.python
 bar          : source.regexp.python
    baz       : source.regexp.python
(?#           : comment.regexp, punctuation.comment.begin.regexp, source.regexp.python
comment 2     : comment.regexp, source.regexp.python
)             : comment.regexp, punctuation.comment.end.regexp, source.regexp.python
