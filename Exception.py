try:
    #fname = 'hello'
    print(fname)
except NameError:
    print("INVALID VAR")
else:
    print('SUCCESS')
finally:
    print('FINALLY')
#open file
try:
    f0 = 'G8_leaders'
    f1 = open(f0)
    print(f2)
except IOError as err:
    print("ERROR OPENING FILE",f0,'ERROR is ',err)
    #exit(200)
except NameError as err:
    print("ERROR OPENING FILE",f0,'ERROR is ',err)
    exit(200)
else:
    print("SUCCESS OPENING FILE",f0)
print("post-operation")
# raise custom exception
try:
    raise NameError('invalid VAR')
except NameError as err:
    print("Error with try block:",err)
