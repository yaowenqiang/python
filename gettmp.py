from subprocess import *
import re
try:
    #Execute Process
    #output = Popen(['pcsensor',"-c"],stdout=PIPE).communicate()[0]
    output = Popen(['uptime'],stdout=PIPE).communicate()[0]
    output = output.strip()
    print(output)
    #Parse results with RegEx
    p = re.compile(r'\s+')
    s = p.split(output)
    print(s)
    s.pop()
    #assign interesting Elements to new VARs
    d = s[0]
    t = s[1]
    tmp = s[3]
    #strip Trailing tem value (f|c)
    tmp2 = tmp[:-1]
    print("DATE: ",d," TIME: ",t," TEMPERATURE: ",tmp)
except OSError as err1:
    print(err1)

