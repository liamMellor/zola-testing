import re 
s = '60 requests  ❘  1.5 MB transferred  ❘  4.07 s (load: 4.10 s, DOMContentLoaded: 4.04 s)'
print re.sub('([0-9]*) requests +\xe2\x9d\x98 +([0-9\\.]*\xe2\x80\x89[MK]B) transferred +\xe2\x9d\x98 +([0-9\\.]*\xe2\x80\x89s) \\(load: ([0-9\\.]*\xe2\x80\x89s), DOMContentLoaded: ([0-9\\.]*\xe2\x80\x89s).*', r'\1\t\2\t\3\t\4\t\5', s)







