"""A plugin for Sublime Text to enhance f-string editing experience.

Specifically, this plugin simplifies typing of escaped curly braces
in an f-string:
   {|}, where | is for cursir, gets replaced with
   {{|, when '{' is typed again.
"""


# Used by `settings/sublime/Default.sublime-keymap`.


import sublime_plugin


class FstringbraceCommand(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view()
        view.run_command('right_delete')
        view.run_command('insert', {'characters': '{'})
