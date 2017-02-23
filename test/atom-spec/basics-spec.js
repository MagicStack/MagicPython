describe("MagicPython basic integration tests", function() {
  var grammar = null;

  beforeEach(function() {
    waitsForPromise(function() {
      return atom.packages.activatePackage("MagicPython")
    });
    runs(function() {
      grammar = atom.grammars.grammarForScopeName("source.python")
    });
  });

  it("recognises shebang on firstline", function() {
    expect(grammar.firstLineRegex.scanner.findNextMatchSync(
      "#!/usr/bin/env python")).not.toBeNull();

    expect(grammar.firstLineRegex.scanner.findNextMatchSync(
      "#! /usr/bin/env python")).not.toBeNull();
  });

  it("parses the grammar", function() {
    expect(grammar).toBeDefined();
    expect(grammar.scopeName).toBe("source.python");
  });
});
