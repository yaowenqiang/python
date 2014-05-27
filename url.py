#Handle URL requests
import urllib.request
#Prepare URL encoded VARs
import urllib.parse

#Get Request
d = 'date'
t = 'time'
temp = 'temp'
url = 'http://192.168.1.109/index.php?'+'%s';
params = urllib.parse.urlencode({'date':d,'time':t,'temp':temp})
#params will resemble:http://192.168.1.1-0/index.php?date=d&time=t&temp=temp
print(params)
#Generate the GET request
print(url)
f = urllib.request.urlopen(url % params)
#evaluate GET  response - Be sure to decode UTF-8
print(f.read().decode('utf-8'))

#Post Request
params_post = params.encode('utf-8')
f = urllib.request.urlopen(url,params_post)
