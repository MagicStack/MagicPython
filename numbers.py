#
# number literals
#

a = 123
a = 000
a = 0o123
a = 0b0101
a = 0x123b

# this is an error
a = 0123
# this is ok
a = 0000

a = 123.456
a = 0.456
a = 000.0001
a = .01234
a = 123e5
a = 123e-5
a = 000123e-005
a = 123.456e+5
a = 0.456e-5

a = 3.14j
a = 10.j
a = 10j
a = .001j
a = 1e100j
a = 3.14e-10j

# python2
a = 123l
a = 123L
a = 0123l

# generic error
a = 123f
