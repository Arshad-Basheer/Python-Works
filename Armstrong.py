arm=0
for i in range(100,2000):
    for j in str(i):
        arm+=int(j)**len(str(i))
    if i==arm:
        print(i,end=" ")
    arm=0

