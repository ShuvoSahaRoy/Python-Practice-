import re

text = "This is a text for regular expression"

match = re.search('text', text)

print(match)
print(match.start())
print(text[10:15])

#split

print(re.split('for',text))

#find

print(re.findall('a','a aba aba bam a'))