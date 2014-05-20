# sys is required to access 'argv'
import sys
# Perform check of number of supplied position parameters
if len(sys.argv) <2:
    print ("Need AT LEST 1 ARG,Supplied:",len(sys.argv),"ARGs",sys.argv[0])
    exit(200)
    #exit('Insufficient ARGs')
elif len(sys.argv) > 2:
    print("You have supplied too many ARGs",len(sys.argv))
    exit('TOO MANY ARGs')
else:
    print ("You have Supplied ",len(sys.argv),"ARGs")
    exit()

