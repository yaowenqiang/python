import pyperclip,sys,re,webbrowser
filename = 'clipboard.txt'
f1 = open(filename,'r')

content = f1.read()
if content == '':
	f2 = open(filename,'w')
	content =str(pyperclip.paste())
	f2.write(content)

n = int(sys.argv[1])-1
p = re.compile(r'\d+')
i = p.findall(content)
print(i)
r = i[n]
paste = "http://huodong.duomi.com/songtaste/?songid="+r
pyperclip.copy(paste)
webbrowser.open("baidu.com")
