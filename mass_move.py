import glob,os,re,sys,shutil
#check for sufficient arguments
if len(sys.argv) <2:
    print("INSUFFICIENT ARGs: NEED 2")
    exit(200)
#initiate glob pattern and iterate
f0 = glob.glob(sys.argv[1])
#for i in f0:
#    print(i)
# Clean up multiple .mov suffixes

for i in f0:
    print("SOURCE FILE: "+i)
    #Define & check Regex
    p = re.compile(r'[_.]')
    j = p.split(i)
    #print(j)
    #Remove first elements
    j.pop(0)
    try:
        for g in range(3):
            j.remove('mov')
    except Exception, e:
        #print("REMOVED ALL VALUES - WILL CONTINUE")
        #print("FINAL J: ",j)
        pass
    #Collapse | join list elements into a string
    d1 = '_' # new delimiter
    m = d1.join(j).title() #joins elements of j based-on d1
    t = 'movs/new/UCBT'+ d1 + m + '.mov'
    #t.title()
    #print(m)
    print("TARGET FILE: "+t)
    #Perform Copy
    try:
        shutil.copyfile(i,t)
    except IOError as err:
        print('ERROR COPYING FILE: ',i,"TO: ",t)
        print('ERROR MESSAGE:',err )
