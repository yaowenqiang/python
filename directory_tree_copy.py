import os,sys
#check for sufficient arguments
if len(sys.argv) <3:
    print("INSUFFICIENT ARGs: NEED 3")
    exit(200)

#Ensure that SOR DIR exists
if os.path.exists(sys.argv[1]):
    #Define SRC VAR DIR as s
    s = sys.argv[1]
else:
    print("DIR: ",sys.argv[1]," DOES NOT EXIST - WILL EXIT")
    exit(200)
if os.path.exists(sys.argv[2]):
    #Define SRC VAR DIR as s
    d = sys.argv[2]
else:
    print("DIR: ",sys.argv[2]," DOES NOT EXIST - WILL EXIT")
    exit(200)
#Use os.walk to map SRC tree
#Note:os.walk returns three VARs,top,directories,files with directories
for root,dirs,files in os.walk(s,topdown=True,onerror=None,followlinks=True):
    #print(root)
    #print(dirs)
    #use os.mkdir to re-create tree
    #t = d +'/' + root # Concatenate DST directory to create
    #print("TARGET IS :" + t)
    #os.mkdir()

    #Use alternate os.mkdirs() to recreate tree
    for name in dirs:
        p = os.path.join(root,name)
        print("CURRENT PATH:",p)
        u = d + "/" + p
        print("FINA PATH:",u)

        try:
            #Create DST tree
            os.makedirs(u)
        except OSError as err:
            print("ERROR GENERATING DST TREE",err)
