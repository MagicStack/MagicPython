describe("python-traceback tests", function() {
  var grammar = null;

  beforeEach(function() {
    waitsForPromise(function() {
      return atom.packages.activatePackage("MagicPython")
    });
    runs(function() {
      grammar = atom.grammars.grammarForScopeName("text.python.traceback")
    });
  });

  it("highlights a traceback line", function() {
    tokens = grammar.tokenizeLines(
      '  File "t.py", line 1, in <module>\n' +
      '    a = 1/0')

    expect(tokens[0][0].value).toBe("  File ");
    expect(tokens[0][0].scopes).toEqual(['text.python.traceback']);

    expect(tokens[0][1].value).toBe('"t.py"');
    expect(tokens[0][1].scopes).toEqual(
      ['text.python.traceback', 'string.python.traceback']);

    expect(tokens[0][2].value).toBe(", line ");
    expect(tokens[0][2].scopes).toEqual(['text.python.traceback']);

    expect(tokens[0][3].value).toBe("1");
    expect(tokens[0][3].scopes).toEqual(
      ['text.python.traceback', 'constant.numeric.python.traceback']);

    expect(tokens[0][4].value).toBe(", in ");
    expect(tokens[0][4].scopes).toEqual(['text.python.traceback']);

    expect(tokens[0][5].value).toBe("<module>");
    expect(tokens[0][5].scopes).toEqual(
      ['text.python.traceback', 'entity.name.function.python.traceback']);

    expect(tokens[1][1].value).toBe("a");
    expect(tokens[1][1].scopes).toEqual(['text.python.traceback']);

    expect(tokens[1][3].value).toBe("=");
    expect(tokens[1][3].scopes).toEqual(
      ['text.python.traceback', 'keyword.operator.assignment.python']);
  });
});
