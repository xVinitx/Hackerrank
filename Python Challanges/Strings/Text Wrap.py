import textwrap

text = input(" ")
maxwidth = int(input())
print(textwrap.fill(text, maxwidth))
