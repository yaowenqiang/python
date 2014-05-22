#Required fo File I/O access
#import os
fname = 'jack'
#for i in fname:
    #print(i)
lastname = 'yao'
full_name = [fname,lastname]
for i in full_name:
    print(i)
for j in range(10):
    print(j)
for j in range(1,11):
    print(j)
for i,j in enumerate(fname):
    print(i,j)
for i in fname:
    print(i)
else:
    print('loop finished')
world_leaders = {'UK':'David Cameron','Germany':'Angela Merkl'}
for i,j in world_leaders.items():
    print(i,j)
else:
    print('finished')
f0 = "G8_leaders"
f1 = open(f0)
for i in f1:
    #print(i,end=' ')
    print(i)
else:
    print('FINISHED WITH DOCUMENTS',f0)

#While loop
count = 0
while count < 10:
    print("Count:",count)
    if count == 6:
        print("CURRENT VALUE is",count,"We will break the loop")
        break
    count += 1
else:
    print("WHILE LOOP OVER")
full_name = 'jack','yao'
for i in full_name:
    print(i)
