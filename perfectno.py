num=int(input("enter a number:"))
s=0
for i in range(1,num):
    if num%i==0:
        s+=i
if s==num:
    print("Perfect")
else:
    print("Not Perfect")