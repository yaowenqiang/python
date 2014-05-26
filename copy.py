import pyperclip,sys,re
content = pyperclip.paste()
n = sys.argv[1]
p = re.compile(r'\d+')
l = p.findall(content)
r = l[n]
print(r)

