import  glob,hashlib,sys
#print(sys.argv[1])
# when run this script  in zsh on linux or mac,the * shoule be escaped,
# for example
# python checksum.py * will not work
# python checksum.py \* will work
try:
    f0 = glob.glob(sys.argv[1])
    for i in f0:
        f1 = open(i,'rb')
        content = f1.read()
        # invoke hashlib
        md5 = hashlib.md5()
        sha1 = hashlib.sha1()

        sha1.update(content);
        sha256 = hashlib.sha256()
        sha256.update(content);
        #feed binary content into hashlib
        md5.update(content);
        #Generate binary and | or hex digest
        print('CHECKSUMS FOR FILE ',i,':')
        print("MD5    : ",md5.hexdigest())
        print("SHA1   : ",sha1.hexdigest())
        print("SHA256 : ",sha256.hexdigest())
except IOError as err:
    print('error opening file ',f0,err)
    exit(200)
#else:
    #print('FILE ',f0,' IS OPEN')
    #print("CONTENT of FILE ",i,": ",content)
    #print("FILE NAME:",i,"\n")
    #try:
        #f0 = "G8_leaders"
        #f0 = glob.glob(sys.argv[1])
        # open file in binary mode
        #f1 = open(f0,'rb')
        #content = f1.read()
        #print(content)
    #except IOError as err:
        #print('error opening file ',f0,err)
        #exit(200)
    #else:
        #print('FILE ',f0,' IS OPEN')
