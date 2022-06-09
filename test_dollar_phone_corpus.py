import re

with open("test_dollar_phone_corpus.txt","r") as f:
    lines=f.read()


match=re.findall(r'(\$\d*\.\d*)|(\$\d*\,\d*\.\d*)|(\$\d* million)|(\$\d* billion)|(\d dollars? and \d cents?)|(\d hundred dollars)',lines)
print(match)

print(len(match))

match2=re.findall(r'(\d{3}-\d{3}-\d{4})|(\d{3}-\d{4})',lines)
print(match2)
print(len(match2))