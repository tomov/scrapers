# used with ptoncs.html -- http://www.cs.princeton.edu/people/faculty
import sys
import re

inp = sys.stdin.read()

t = re.compile("E-mail</a>:</td>\n<td align=left>([a-zA-Z0-9]*)</td></tr>")
emails = re.findall(t, inp)
for s in emails:
    print s + '@cs.princeton.edu, ' + s + '@princeton.edu'

print '\n\n\n\n'

t = re.compile("<a href=\"http://www.cs.princeton.edu/~[a-zA-z0-9]*/\">([a-zA-Z0-9 ]*)</a>|<td class=\"people people_center\" valign=top nowrap>\n([a-zA-Z0-9 ]*)\n<br>")
names = re.findall(t, inp)
for s in names:
    name = s[0] if s[0] else s[1]
    last_name = name.split(' ')[1] if name.split(' ')[1] else name.split(' ')[2]  # double space...
    print last_name
