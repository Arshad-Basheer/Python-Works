#function is a block of statement used to perform an operation or a task
#def fnname (parameters):
    # "fn doctring"
    # fn body
    #
    # return [expression]

# def addition():
#     "Addition of two numbers"
#     num1=int(input("enter a number:"))
#     num2=int(input("enter another number:"))
#     sum=num1+num2
#     print(f"sum={sum}")
#     return
# addition()


# def display():
#     "displaying youe name"
#     print("Hello Arshad")
# display()

# def factorial():
#     "factorial of a number"
#     num1=int(input("enter a number"))
#     s=num1
#     for i in range(num1-1,0,-1):
#         s*=i
#     print(s)
#     return
# factorial()


# def occurence():
#     s=input("enter a string")
#     count=0
#     for i in s:
#         if i=="a":
#             count+=1
#     print(count)
#     return
# occurence()

# def sumlist():
#     l=[89,45,67,12]
#     s=0
#     for i in l:
#         s+=i
#     print(s)
#     return
# sumlist()


# def prime():
#     n=int(input("enter a number:"))
#     for i in range(2,n):
#         if n%i==0:
#             print("not prime")
#             break
#     else:
#         print("prime")
# prime()


#define a function that takes three arguments and (amount,rate,year) and find the simple interest value
# def simple_interest(a,b,c):
#     si=a*b*c/100
#     print(si)
#     return
#
# p=int(input("enter the amount:"))
# n=int(input("enter the rate:"))
# r=int(input("enter the year:"))
# simple_interest(p,n,r)

# def simple_interest(a,b,c):
#     si=a*b*c/100
#     return si
#
# p=int(input("enter the amount:"))
# n=int(input("enter the rate:"))
# r=int(input("enter the year:"))
# res=simple_interest(p,n,r)
# print(res)


# def product(a,b,c):
#     return a*b*c
# res=product(2,3,4)
# print(res)

# def occurence(str1,a):
#     count=0
#     for i in str1:
#         if i==a:
#             count+=1
#     return count
# str1=input("enter a string: ")
# cha=input("enter the character: ")
# b=occurence(str1,cha)
# print(f"no of occurences = {b}")

# #define a function that takes a list as arguments and returns a new list containing unique elements from list
# def unique(l):
#     new=[]
#     for i in l:
#         if i not in new:
#             new.append(i)
#     return new
# l=[12,34,78,12,67,34,90,23]
# new_list= unique(l)
# print(new_list)


#define a function that takes 2 lists as arguments and print common elements
# l=[12,34,56,78,90]
# l1=[90,34,11,57,45]
# def common(l,l1):
#     for i in l:
#         if i in l1:
#             print(i,end=" ")
# common(l,l1)


# def fun(n,a):
#     print("Name=",n)
#     print("Age=",a)
# fun(a=22,n="Arshad")

# def fun(*args):
#     print(args)
# fun(1,2,3,4)

# def fun(**kwargs):
#     print(*kwargs)
# fun(name="arshad",age=23)

def fun(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
res=fun(1,2,3,4,5)
print(res)
