#
# test signatures of class and funciton definitions
#

->

# various funciton declarations
#

def myfunc(self,            # gotta have self
           param1="value",  # values are cool
           param2=True,     # or False, whatever
           **kwargs):       # you never know

def some_call(a, b, *args, **kwargs):
    pass

def result_annot() -> qqq[None]:
    pass

def annot(a:'simple'=123, b:('abc' 'def')=123, c:{'key': 555}=None, #foo
          d:woot(42)=toow(24), e=fff) -> foo(1):
    pass

def annot(a:'simple'=123, b:1 \
                            'def'=123, c:{'key': 555}=None, #foo
          d:woot(42)=toow(24), e=fff) -> foo(1):
    pass

def def(): pass

lambda

anon = lambda: 42

anon = lambda a : 1

anon = lambda a, b=7777, *args, **kwargs: None

# bad
anon = lambda -> qqq[None]: None

# ok
anon = lambda a=123, b=123, c={'key': 555}, \
              d=toow(24), e=fff: None

anon = lambda a=123, b=123, c={'key':
                                 555}, d=toow(24), e=fff: None

# bad
anon = lambda a=123, b=123, c={'key': 555}, f=2, \
              d=toow(24), e=fff -> foo(1): None

anon = lambda a=123, b=123, c={'key': 555}, f=2,
              d=toow(24), e=fff -> foo(1): None

anon = lambda a=123, b=123, c={'key': 555}, f=2
              d=toow(24), e=fff: None

anon = lambda a=123, b=123, c={'key': 555}, f=2, # foooo
              d=toow(24), e=fff: None

anon = lambda a=123, b=123, c={'key': 555},
              d=toow(24), e=fff: None

# line cont
#

1 + \ sdgfsdf

1 + \
 3

# funciton calls
#

some_call(1)
some_call(1, 3)
some_call(a=2, b={'q': 42})
some_call(a=2, b={'q': 42}, **kwargs)
some_call(4, *args)

''.format(1)
''.format(1, 3)
''.format(a=2, b={'q': 42})
''.format(a=2, b={'q': 42}, **kwargs)
''.format(4, *args)

# illegal member access
foo.class(a)
foo.and()
foo.if

# arrays and members
#

arr = [1, 2, 3]
arr[foo(2)]
arr2 = [i for i in range(7) if i != 3]

# various class declarations
#

class Foo: pass
class Foo(object): pass
class Foo -> None: pass

print >>sys.stderr, "fatal error"
123123l
(a, *rest, b) = range(5)
raise SecondaryException() from primary_exception

class class:
    pass
r''

# name clashing is legal, but questionable, so at least it should be visible
class Exception: pass

class Spam(Foo, Bar={'very': 'odd'}, Exception, wefwf=23, metaclass=QQQ):

    def __init__(self, a:('abc' 'def')=123, boo: 'abc'

                                                 'def' = foo(n(m=0), baz=
                                                    13)):
        self.all_options = set()

    def __await__(self):
        pass

    async

    async def

    # async def foo()

    async def foo():
        a = 1
        async for a in b:
            async with b:
                await print(a)

        ssl.PROTOCOL_v2.hgyhgh

        HTTPProtocol

class Woot(Foo, Bizarre(42), Bar=foo(aaa=1, bbb=4), wefwf=23, metaclass=QQQ):
    pass

# decorators
#

@some_decorator
@some_decorator # with comment
@some.class.decorator
@some_decorator(1)
@some.decorator   (1, 3)
@some.decorator(a=2, b={'q': 42})
@some_decorator(a=2, b={'q': 42}, **kwargs)
@some_decorator(4, *args)
@classmethod
def decorated(): pass

SranError
