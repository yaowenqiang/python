import platform,re,sys
#Obtain system hostname
h = platform.node()
#print(h)

#ensure that platform is Windows
s = platform.system()
p = re.compile(r'win.',re.IGNORECASE)
if p.search(s):
    print("platform is ",s)
else:
    print("This script is restricted to Windows platform")

#Ensure 64-bit platform
bits = platform.architecture()[0][0:2]
#print(bits)
p = re.compile(r'^64')
if p.search(bits):
    print("BITS; ",bits)
else:
    print("SCRIPT:",sys.argv[0]," REQUIRES 64-bit platform")
#Ensure Release of Windows >= 7
r = int(platform.release()[0])
minr = int(7)
if r >= minr:
    print("Platform Version:",s,r,bits)
uname = platform.uname()
d1 = ''
u = uname.join(uname)
print(u)
