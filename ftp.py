from ftplib import FTP_TLS
# TODO learn vsftpd first
import os
#Define credentials
user = 'jack'
secret = '123456'
host = '192.168.1.113'
try:
    #instantiate FTPS
    #ftps = FTP_TLS(host,user,secret)
    ftps = FTP_TLS(host)
    # TODO check why the next line not work
    #See http://stackoverflow.com/questions/10207628/python-module-ftplib-ftp-tls-error-530
    #Try TLS Lite or M2Crypto both are FTP/TLS client and server.

    #ftps.login(user,secret)

    ftps.sendcmd('USER ' + user)
    ftps.sendcmd('PASS ' + secret)
    print(ftps.getwelcome())
    print('CURRENT WORKING DIRECTORY IS:',ftps.pwd())
    #Enable data encryption
    # TODO solve the encryption problem
    #ftps.prot_p()
    #define default DIR
    d = 'feeds'
    #Change to default DIR
    ftps.cwd(d)
    #Build list of files on servers
    l = ftps.nlst()
    l.sort()
    for i in l:
        print(i)
    #Assign last element to var
    litem = len(l)-1
    print("MOST RECENT FILE ON SERVER IS; ",l[litem])

    g = l[litem]
    #Define local file
    t = d + '/' + g
    if os.path.exists(t):
        print("FILE" ,g," EXISTS,WILL NOT DOWNLOAD FROM HOST:",host)
    else:
        print("WILL DOWNLOAD FILE:",g)
        #Construct 'RETR' string for FTP download function
        getstring = 'RETR ' + g
        print(getstring)
        ftps.retrbinary(getstring,open(t,'wb').write)
    #Close Session
    ftps.close()
except IOError as err:
    print("ERROR RETRIEVING FILES ",err)
