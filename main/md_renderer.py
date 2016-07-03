# coding:utf-8

import misaka as m
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

# Create a custom renderer
class BleepRenderer(m.HtmlRenderer):
    def block_code(self, text, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                text.strip()
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = HtmlFormatter()
        return highlight(text, lexer, formatter)

renderer = BleepRenderer()
md = m.Markdown(renderer, extensions=('fenced-code',))

if __name__ == '__main__':
    # And use the renderer
    print(md("""```python
    # -*- coding:utf-8 -*-
    import os
    import sys
    ```"""))