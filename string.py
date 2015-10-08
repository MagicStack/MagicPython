#
# test pyhton string highlighting
#

'simple string'
u'simple string'
b'simple string'
r'simple string'
br'simple string'

# single quote with line continuation
#
'simple string \
foo \' \" \a \b \c \f \n \r \t \v \5 \55 \555 \05 \005'

'bad string
foo \' \" \a \b \c \f \n \r \t \v \5 \55 \555 \05 \005'

b'simple string \
foo \' \" \a \b \c \f \n \r \t \v \5 \55 \555 \05 \005'

b'bad string
foo \' \" \a \b \c \f \n \r \t \v \5 \55 \555 \05 \005'

r'simple string \
foo \'

r'bad string
foo \'

# multiline strings
#
'''
multiline 'unicode' string \

    \xf1 \u1234aaaa \U1234aaaa

    \N{BLACK SPADE SUIT}
'''

b'''
multiline 'binary' string \

    \xf1 \u1234aaaa \U1234aaaa

    \N{BLACK SPADE SUIT}
'''

r'''
multiline 'raw' string \

    \xf1 \u1234aaaa \U1234aaaa

    \N{BLACK SPADE SUIT}
'''

# formatting
#
'%i' % 42
'%(language)s has %(number)03d quote types.' % {'language': "Python",
                                                "number": 2}
b'%(language)s has %(number)03d quote types.' % {'language': "Python",
                                                "number": 2}
r'%(language)s has %(number)03d quote types.' % {'language': "Python",
                                                "number": 2}

'{(([ ]:X>+10d}'.format(**{'((': {' ': 42}})
'{(([ ]:Xd>+10d}'.format(**{'((': {' ': 42}}) # bad formatting
'{(([ ]:Xd}'.format(**{'((': {' ': 42}})
'normal {{ normal }} normal {fo.__add__!s}'.format(fo='qqq')

# double-quote style
#
"simple string"
u"simple string"
b"simple string"
r"simple string"
br"simple string"

# single quote with line continuation
#
"simple string \
foo \' \" \a \b \c \f \n \r \t \v \5 \55 \555 \05 \005"

"bad string
foo \' \" \a \b \c \f \n \r \t \v \5 \55 \555 \05 \005"

b"simple string \
foo \' \" \a \b \c \f \n \r \t \v \5 \55 \555 \05 \005"

b"bad string
foo \' \" \a \b \c \f \n \r \t \v \5 \55 \555 \05 \005"

r"simple string \
foo \"

r"bad string
foo \"

# multiline strings
#
"""
multiline "unicode" string \

    \xf1 \u1234aaaa \U1234aaaa

    \N{BLACK SPADE SUIT}
"""

b"""
multiline "binary" string \

    \xf1 \u1234aaaa \U1234aaaa

    \N{BLACK SPADE SUIT}
"""

r"""
multiline "raw" string \

    \xf1 \u1234aaaa \U1234aaaa

    \N{BLACK SPADE SUIT}
"""

# formatting
#
"%i" % 42
"%(language)s has %(number)03d quote types." % {'language': "Python",
                                                "number": 2}
b"%(language)s has %(number)03d quote types." % {'language': "Python",
                                                "number": 2}
r"%(language)s has %(number)03d quote types." % {'language': "Python",
                                                "number": 2}

"{(([ ]:X>+10d}".format(**{'((': {' ': 42}})
"{(([ ]:Xd>+10d}".format(**{'((': {' ': 42}}) # bad formatting
"{(([ ]:Xd}".format(**{'((': {' ': 42}})
"normal {{ normal }} normal {fo.__add__!s}".format(fo='qqq')
