import pyperclip,sys,os,re,webbrowser
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
#print(i)
r = i[n]
paste = "http://huodong.duomi.com/songtaste/?songid="+r
pyperclip.copy(paste)
#webbrowser.open("baidu.com")
os.startfile(paste)
#TODO make it corss-platform
#TODO fix open twice bug
#if sys.platform=='win32':
#    os.startfile(url)
#elif sys.platform=='darwin':
#    subprocess.Popen(['open', url])
#else:
#    try:
#        subprocess.Popen(['xdg-open', url])
#    except OSError:
#        print 'Please open a browser on: '+url
#http://stackoverflow.com/questions/4216985/python-call-to-operating-system-to-open-url