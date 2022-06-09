import re

with open("test.txt","r") as f:
    lines=f.read()


match=re.findall(r'(\d dollars? and \d cents?)',lines)
print(match)

print(len(match))