import asyncio


def showcase():
    """Some code to showcase the syntax.

    Docstrings are recognized and have an additional scope.
    Color schemas can render them differently from other strings.

    HACK doctests are highlighted too.

        >>> print('''hello
        ... world''')
    """

    @decorator(param='spam')
    async def coroutine(db:aio_db.DatabaseConnection) -> List[str]:
        r"""A coroutine."""

        await logger.log('working\x12with %r', aio_db)

        async with db.transaction():
            print('Result: {result!r}'.format(result=
                await db.query(...)))

    # a regular expression
    get_regex = lambda: re.compile(
        r"""\A
            word
            (?:                   # a comment
               (?P<fill>.)?
               (?P<align>[<>=^])  (?# another comment)
            )?
            another word\.\.\.
            (?:\.(?P<precision>0|(?!0)\d+))?
        \Z""",
        re.VERBOSE | re.DOTALL)

    # NOTE Numbers with leading zeroes are invalid in Python3,
    # use 0o...
    answer = func(0xdeadbeef + 0b0010001 + 0123 + 0o123 +
                  # complex numbers
                  .10e12 + 2j) @ mat

    raw_string = R'''No escapes '\' in this \one'''

    return NotImplemented
