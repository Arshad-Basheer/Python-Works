num=int(input("enter a number:"))

if len(str(num))==2:
    print("it is a 2 digit number")
elif len(str(num))==3:
    print("it is a 3 digit number")
elif len(str(num))==4:
    print("it is a 4 digit number")
else:
    print("it is is 2-4 digit number")