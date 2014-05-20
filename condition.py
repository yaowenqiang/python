# sys is required to access 'argv'
import sys
# Perform check of number of supplied position parameters
#assign length of sys.argv to simple var
leng1 = len(sys.argv)
if leng1 <2:
    print ("Need AT LEST 1 ARG,Supplied:",leng1,"ARGs",sys.argv[0])
    exit(200)
    #exit('Insufficient ARGs')
elif leng1 > 2:
    print("You have supplied too many ARGs",leng1)
    exit('TOO MANY ARGs')
else:
    print ("You have Supplied ",leng1,"ARGs")
    #pass keeps the functions/script going without doing any thing
    pass
    #help('pass')
    #exit()
    print("You have Passed")

