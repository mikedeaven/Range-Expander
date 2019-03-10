import re

import sublime
import sublime_plugin

def expand_single_range(match):
    rangeStart = int(match.group(1))
    print(rangeStart)
    rangeEnd = int(match.group(2))
    values = [str(x) for x in range(rangeStart, rangeEnd + 1 if rangeEnd > rangeStart else rangeEnd - 1, 1 if rangeEnd > rangeStart else -1)]
    return ', '.join(values)

def expand_in_text(text):
    return re.sub(r'(\d+)-(\d+)', expand_single_range, text)

class ExpandCommand(sublime_plugin.TextCommand):
    def run(self, edit):
       view = self.view

       region = view.sel()[0]
       text = view.substr(region)
       print(text)

       view.replace(edit, region, expand_in_text(text))