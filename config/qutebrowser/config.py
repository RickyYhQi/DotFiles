# Autogenerated config.py
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Uncomment this to still load settings configured via autoconfig.yml
# config.load_autoconfig()

# The proxy to use. In addition to the listed values, you can use a
# `socks://...` or `http://...` URL.
# Type: Proxy
# Valid values:
#   - system: Use the system wide proxy.
#   - none: Don't use any proxy

# The page(s) to open at the start.
# Type: List of FuzzyUrl, or FuzzyUrl
c.url.start_pages = ['https://www.baidu.com/']

# Bindings for normal mode
config.bind('<ctrl+i>', 'open-editor')
config.bind('<ctrl+o>', 'back')
config.bind('\\;', 'spawn --userscript ydcv')
config.bind('t', 'set-cmd-text -s :open -t')

# Bindings for insert mode
config.bind('<ctrl+k>', 'fake-key <Shift-End> ;; fake-key <Delete>', mode='insert')
config.bind('<ctrl+u>', 'fake-key <Shift+Home> ;; fake-key <Delete>', mode='insert')
config.bind('<ctrl+w>', 'fake-key <Ctrl-backspace>', mode='insert')
