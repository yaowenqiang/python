import re
try:
    f0 = 'G8_leaders'
    #f1 = open(f0,('r,w(clobber),a(append),r+(rad+write)'))
    f1 = open(f0,'r')
    f2 = 'G8_leaders2'
    f3 = open(f2,'w');
    #f1.read() # returns file as a single string
    #f1.readlines() # returns 1 line per instance
    #loop over f1.readlines();
    for i in f1.readlines():
        #RegEx to suppress BLANK lines
        if re.search('.',i):
        # dump line from f1
            #Define compiled RegEx Pattern
            p = re.compile(r"\W+")
            # Split current record,removing trailings \n
            j = p.split(i[:-1])
            j.insert(2,"G20")
            j.append("G8")
            print(j)
            #concatenate elements
            newrecord = j[0] + "\t" + j[1] + "\t" + j[2] + "\t" + j[3]
            print(newrecord)
            #f3.write(newrecord)
            #print(i)
            # Modify printed line
            #print(i[:-1]) #Strip trailing characters
            #Define modified field
            #newrecord = i[:-1] + '\tG8\n'
            #print(newrecord)
            f3.write(newrecord)

    #write string to f1
    #nrerecord = "Sarkozy\tNicolas\tFrance\n"
    #f3.write(nrerecord)
except IOError as err:
    print('Error opening file f0')


