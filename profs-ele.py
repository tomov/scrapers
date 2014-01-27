# used with ptonele.html -- http://www.princeton.edu/ee/people/?display=1 
import sys
import re

inp = sys.stdin.read()

t = re.compile("<a href=\"mailto:([a-zA-Z0-9._@]*)\">")
emails = re.findall(t, inp)
for s in emails:
    print s

print '\n\n\n\n'

t = re.compile("<p><a href=\"/ee/people/display_person/\?netid=[a-z0-9]*\">([a-zA-Z0-9 .-]*)</a><br>")
names = re.findall(t, inp)
for s in names:
    name = s 
    last_name = name.split(' ')[len(name.split(' ')) - 1]
    print last_name
