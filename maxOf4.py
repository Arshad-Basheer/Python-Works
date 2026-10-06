a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
d=int(input("enter the fourth number"))

if a>b and a>c and a>d:
    print(a,"is greater")
elif b>c and b>d:
    print(b,"is greater")
elif c>d:
    print(c,"is greater")
else:
    print(d,"is greater")