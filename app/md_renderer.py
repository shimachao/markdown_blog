# coding:utf-8

import misaka as m
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name

class HighlighterRenderer(m.HtmlRenderer):
    def blockcode(self, text, lang):
        if not lang:
            return '\n<pre><code>{}</code></pre>\n'.format(text.strip())

        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = HtmlFormatter()

        return highlight(text, lexer, formatter)

renderer = HighlighterRenderer()
md = m.Markdown(renderer, extensions=('fenced-code',))

if __name__ == '__main__':
    # And use the renderer
    print(md("""```python
    # -*- coding:utf-8 -*-
    import os
    import sys
    print('hello world')
    ```"""))