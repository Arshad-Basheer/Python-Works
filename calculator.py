num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
op=input("enter the operator:")

if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    print(num1/num2)
else:
    print("invalid operator")
