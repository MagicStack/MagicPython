# And now something fun!

CookiePattern = re.compile(r"""
    (?x)                           # This is a verbose pattern
    \s*                            # Optional whitespace at start of cookie
    (?P<key>                       # Start of group 'key'
    [""" + _LegalKeyChars + r"""]+?   # Any word of at least one letter
    )                              # End of group 'key'
    (                              # Optional group: there may not be a value.
    \s*=\s*                          # Equal Sign
    (?P<val>                         # Start of group 'val'
    "(?:[^\\"]|\\.)*"                  # Any doublequoted string
    |                                  # or
    \w{3},\s[\w\d\s-]{9,11}\s[\d:]{8}\sGMT  # Special case for "expires" attr
    |                                  # or
    [""" + _LegalValueChars + r"""]*      # Any word or empty string
    )                                # End of group 'val'
    )?                             # End of optional value group
    \s*                            # Any number of spaces.
    (\s+|;|$)                      # Ending either at space, semicolon, or EOS.
    """, re.ASCII)                 # May be removed if safe.


#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 And now something fun! : comment.line.number-sign.python, source.python
              : source.python
CookiePattern  : source.python
=             : keyword.operator.assignment.python, source.python
 re.          : source.python
compile       : meta.function-call.python, source.python
(             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
r             : meta.function-call.arguments.python, meta.function-call.python, source.python, storage.type.string.python, string.regexp.quoted.triple.python
"""           : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.python, string.regexp.quoted.triple.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
(?x)          : meta.function-call.arguments.python, meta.function-call.python, source.python, storage.modifier.flag.regexp, string.regexp.quoted.triple.python
                            : meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
#             : comment.line.number-sign.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.comment.python, source.python, string.regexp.quoted.triple.python
 This is a verbose pattern : comment.line.number-sign.python, meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
\s            : meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python, support.other.escape.special.regexp
*             : keyword.operator.quantifier.regexp, meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
                             : meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
#             : comment.line.number-sign.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.comment.python, source.python, string.regexp.quoted.triple.python
 Optional whitespace at start of cookie : comment.line.number-sign.python, meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
(             : meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, punctuation.parenthesis.named.begin.regexp support.other.parenthesis.regexp, source.python, string.regexp.quoted.triple.python
?P<key>       : entity.name.tag.named.group.regexp, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
                        : meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
#             : comment.line.number-sign.python, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, punctuation.definition.comment.python, source.python, string.regexp.quoted.triple.python
 Start of group 'key' : comment.line.number-sign.python, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
              : meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
[             : constant.other.set.regexp punctuation.character.set.begin.regexp, meta.character.set.regexp, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
"""           : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.python, string.regexp.quoted.triple.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python
+             : keyword.operator.python, meta.function-call.arguments.python, meta.function-call.python, source.python
 _LegalKeyChars  : meta.function-call.arguments.python, meta.function-call.python, source.python
+             : keyword.operator.python, meta.function-call.arguments.python, meta.function-call.python, source.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python
r             : meta.function-call.arguments.python, meta.function-call.python, source.python, storage.type.string.python, string.regexp.quoted.triple.python
"""           : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.python, string.regexp.quoted.triple.python
]             : meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
+?            : keyword.operator.quantifier.regexp, meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
#             : comment.line.number-sign.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.comment.python, source.python, string.regexp.quoted.triple.python
 Any word of at least one letter : comment.line.number-sign.python, meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
    )                               : meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
#             : comment.line.number-sign.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.comment.python, source.python, string.regexp.quoted.triple.python
 End of group 'key' : comment.line.number-sign.python, meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
(             : meta.function-call.arguments.python, meta.function-call.python, punctuation.parenthesis.begin.regexp support.other.parenthesis.regexp, source.python, string.regexp.quoted.triple.python
                               : meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
#             : comment.line.number-sign.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.comment.python, source.python, string.regexp.quoted.triple.python
 Optional group: there may not be a value. : comment.line.number-sign.python, meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
\s            : meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python, support.other.escape.special.regexp
*             : keyword.operator.quantifier.regexp, meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
=             : meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
\s            : meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python, support.other.escape.special.regexp
*             : keyword.operator.quantifier.regexp, meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
                           : meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
#             : comment.line.number-sign.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.comment.python, source.python, string.regexp.quoted.triple.python
 Equal Sign   : comment.line.number-sign.python, meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
(             : meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, punctuation.parenthesis.named.begin.regexp support.other.parenthesis.regexp, source.python, string.regexp.quoted.triple.python
?P<val>       : entity.name.tag.named.group.regexp, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
                          : meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
#             : comment.line.number-sign.python, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, punctuation.definition.comment.python, source.python, string.regexp.quoted.triple.python
 Start of group 'val' : comment.line.number-sign.python, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
    "         : meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
(?:           : meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, punctuation.parenthesis.non-capturing.begin.regexp support.other.parenthesis.regexp, source.python, string.regexp.quoted.triple.python
[             : constant.other.set.regexp punctuation.character.set.begin.regexp, meta.character.set.regexp, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
^             : keyword.operator.negation.regexp, meta.character.set.regexp, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
\\            : constant.character.escape.regexp, meta.character.set.regexp, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
"             : constant.character.set.regexp, meta.character.set.regexp, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
]             : constant.other.set.regexp punctuation.character.set.end.regexp, meta.character.set.regexp, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
|             : keyword.operator.disjunction.regexp, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
\\            : constant.character.escape.regexp, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
.             : meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python, support.other.match.any.regexp
)             : meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, punctuation.parenthesis.non-capturing.end.regexp support.other.parenthesis.regexp, source.python, string.regexp.quoted.triple.python
*             : keyword.operator.quantifier.regexp, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
"                   : meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
#             : comment.line.number-sign.python, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, punctuation.definition.comment.python, source.python, string.regexp.quoted.triple.python
 Any doublequoted string : comment.line.number-sign.python, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
              : meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
|             : keyword.operator.disjunction.regexp, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
                                   : meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
#             : comment.line.number-sign.python, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, punctuation.definition.comment.python, source.python, string.regexp.quoted.triple.python
 or           : comment.line.number-sign.python, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
              : meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
\w            : meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python, support.other.escape.special.regexp
{3}           : keyword.operator.quantifier.regexp, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
,             : meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
\s            : meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python, support.other.escape.special.regexp
[             : constant.other.set.regexp punctuation.character.set.begin.regexp, meta.character.set.regexp, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
\w            : meta.character.set.regexp, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python, support.other.escape.special.regexp
\d            : meta.character.set.regexp, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python, support.other.escape.special.regexp
\s            : meta.character.set.regexp, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python, support.other.escape.special.regexp
-             : constant.character.set.regexp, meta.character.set.regexp, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
]             : constant.other.set.regexp punctuation.character.set.end.regexp, meta.character.set.regexp, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
{9,11}        : keyword.operator.quantifier.regexp, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
\s            : meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python, support.other.escape.special.regexp
[             : constant.other.set.regexp punctuation.character.set.begin.regexp, meta.character.set.regexp, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
\d            : meta.character.set.regexp, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python, support.other.escape.special.regexp
:             : constant.character.set.regexp, meta.character.set.regexp, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
]             : constant.other.set.regexp punctuation.character.set.end.regexp, meta.character.set.regexp, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
{8}           : keyword.operator.quantifier.regexp, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
\s            : meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python, support.other.escape.special.regexp
GMT           : meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
#             : comment.line.number-sign.python, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, punctuation.definition.comment.python, source.python, string.regexp.quoted.triple.python
 Special case for "expires" attr : comment.line.number-sign.python, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
              : meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
|             : keyword.operator.disjunction.regexp, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
                                   : meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
#             : comment.line.number-sign.python, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, punctuation.definition.comment.python, source.python, string.regexp.quoted.triple.python
 or           : comment.line.number-sign.python, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
              : meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
[             : constant.other.set.regexp punctuation.character.set.begin.regexp, meta.character.set.regexp, meta.function-call.arguments.python, meta.function-call.python, meta.named.regexp, source.python, string.regexp.quoted.triple.python
"""           : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.python, string.regexp.quoted.triple.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python
+             : keyword.operator.python, meta.function-call.arguments.python, meta.function-call.python, source.python
 _LegalValueChars  : meta.function-call.arguments.python, meta.function-call.python, source.python
+             : keyword.operator.python, meta.function-call.arguments.python, meta.function-call.python, source.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python
r             : meta.function-call.arguments.python, meta.function-call.python, source.python, storage.type.string.python, string.regexp.quoted.triple.python
"""           : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.python, string.regexp.quoted.triple.python
]             : meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
*             : keyword.operator.quantifier.regexp, meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
#             : comment.line.number-sign.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.comment.python, source.python, string.regexp.quoted.triple.python
 Any word or empty string : comment.line.number-sign.python, meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
    )                                 : meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
#             : comment.line.number-sign.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.comment.python, source.python, string.regexp.quoted.triple.python
 End of group 'val' : comment.line.number-sign.python, meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
    )         : meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
?             : keyword.operator.quantifier.regexp, meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
                              : meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
#             : comment.line.number-sign.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.comment.python, source.python, string.regexp.quoted.triple.python
 End of optional value group : comment.line.number-sign.python, meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
\s            : meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python, support.other.escape.special.regexp
*             : keyword.operator.quantifier.regexp, meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
                             : meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
#             : comment.line.number-sign.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.comment.python, source.python, string.regexp.quoted.triple.python
 Any number of spaces. : comment.line.number-sign.python, meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
(             : meta.function-call.arguments.python, meta.function-call.python, punctuation.parenthesis.begin.regexp support.other.parenthesis.regexp, source.python, string.regexp.quoted.triple.python
\s            : meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python, support.other.escape.special.regexp
+             : keyword.operator.quantifier.regexp, meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
|             : keyword.operator.disjunction.regexp, meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
;             : meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
|             : keyword.operator.disjunction.regexp, meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
$             : meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python, support.other.match.end.regexp
)             : meta.function-call.arguments.python, meta.function-call.python, punctuation.parenthesis.end.regexp support.other.parenthesis.regexp, source.python, string.regexp.quoted.triple.python
                       : meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
#             : comment.line.number-sign.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.comment.python, source.python, string.regexp.quoted.triple.python
 Ending either at space, semicolon, or EOS. : comment.line.number-sign.python, meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
              : meta.function-call.arguments.python, meta.function-call.python, source.python, string.regexp.quoted.triple.python
"""           : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.python, string.regexp.quoted.triple.python
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.python
 re.          : meta.function-call.arguments.python, meta.function-call.python, source.python
ASCII         : constant.other.caps.python, meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python
                  : source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 May be removed if safe. : comment.line.number-sign.python, source.python
