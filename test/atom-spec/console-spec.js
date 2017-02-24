describe("python-console tests", function() {
  var grammar = null;

  beforeEach(function() {
    waitsForPromise(function() {
      return atom.packages.activatePackage("MagicPython")
    });
    runs(function() {
      grammar = atom.grammars.grammarForScopeName("text.python.console")
    });
  });

  it("highlights >>>", function() {
    tokens = grammar.tokenizeLines(">>> print")

    expect(tokens[0][0].value).toBe(">>>");
    expect(tokens[0][0].scopes).toEqual(
      ['text.python.console', 'punctuation.separator.prompt.python.console']);

    expect(tokens[0][1].value).toBe(" ");
    expect(tokens[0][1].scopes).toEqual(['text.python.console']);

    expect(tokens[0][2].value).toBe("print");
    expect(tokens[0][2].scopes).toEqual(
      ['text.python.console', 'support.function.builtin.python']);
  });
});
