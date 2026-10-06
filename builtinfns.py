# # # # #Write a program to find the position of a character in a string
# s=input("enter the string:")
# ch=input("enter the character:")
# print(s.index(ch))


# # # # #write a program to find the count of character in  a string
# s=input("enter the string:")
# ch=input("enter the character:")
# print(s.count(ch))

# # # #create a random 5 digit otp number and print otp number
import random
# print("OTP:",random.randint(10000,99999))

# # #create a list of  5 random 3 digit numbers
# l=[]
# for _ in range(5):
#     l.append((random.randint(100,999)))
# print(l)

# # #create a dictionary where keys are words and values are length of each word from the string
# #
# s="python coding is easy and fun"
# #
# # #new={'python':6,'coding':6,'is':2,'easy':4,'and':3,'fun':3}
# new={i:len(i) for i in s.split()}
# print(new)

# # # #create a dictionary where keys are each character and values are number of occurence of each character
# s="hello world"
# # d={'h':1,'e':1,'l':3,'o':2,'':1,'w':1,'r':1,'d':1}
# d={i:s.count(i) for i in s if i != " "}
# print(d)


# # #write a program to find the number of digits,letters,and spaces in a string
#
# s="sdfghjk3456789  dffghjkl345678"
# dig=0
# let=0
# sp=0
# for i in s:
#     if i.isdigit():
#         dig+=1
#     elif i.isalpha():
#         let+=1
#     elif i.isspace():
#         sp+=1
# print(f"No of letters = {let}")
# print(f"No of digits = {dig}")
# print(f"No of spaces = {sp}")



# # # Given a list
# l=[['amal',23,30000],['arun',25,50000],['anu',24,40000]]
# # # # create a list of salaries
# # # # find the maximum salary
# # # # find minimum salary
# salary=[]
# for i in l:
#     salary.append(i[2])
# print(f"Maximum salary = {max(salary)}")
# print(f"Minimum salary = {min(salary)}")



# #Given a dictionary
# d={'arun':34,'amal':45,'anu':40,'kiran':25,'manu':30}
#
# # create a new list of students whose mark>=40
# new=[i for i in d if d[i]>=40]
# print(new)
#
#
# #Given two lists
# l1=[11,27,34,45,56]
# l2=[27,34,86,91]
# for i in l1:
#     if i in l2:
#         print(i,end=" ")
# Find Common elements


# #Given
# l=[23,45,67,12,90,56]
# l.sort()
# print(f"Second largest number = {l[-2]}")
# print(f"second smallest number = {l[1]}")

#find second largest number
#find second smallest number

a={1:2,2:3,3:4}
for i,j in a.items():
    print(i)
    print(j)