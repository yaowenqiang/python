import glob,os,re,sys
#check for sufficient arguments
if len(sys.argv) <2:
    print("INSUFFICIENT ARGs: NEED 2")
    exit(200)
try:
    #initiate glob pattern and iterate
    #glob ignores current and parent nodes:'.' && '..'
    f0 = glob.glob(sys.argv[1])
    for i in f0:
        #Note "\W" - will extract:[a-zA-Z_l]
        #note:Generate a slight variation on RegEx:"\W"
        print("SOURCE FILE: ",i)
        p = re.compile(r'[\W+^_]')
        #finds the RegEx patterns in strings(file name)
        j = p.findall(i)

        #remove duplicates
        s = set(j)
        print("HERE IS THE FINAL SET OF DELIMITER: ",s)
except IOError as err:
    print("ERROR OPENING FILE",err)
