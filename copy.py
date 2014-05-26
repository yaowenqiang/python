import pyperclip,sys,re
content =str(pyperclip.paste())
n = int(sys.argv[1])-1
p = re.compile(r'\d+')
i = p.findall(content)
print(i)
r = i[n]
paste = "http://huodong.duomi.com/songtaste/?songid="+r
pyperclip.copy(paste)
