# # # # Q1.Define a function that takes 2 numbers and returns their product
# def product(a,b):
#     return a*b
# num1=int(input("enter the first number:"))
# num2=int(input("enter the second number:"))
# res=product(num1,num2)
# print("Profuct = ",res)


# # Q2.Define a function that takes a string and returns number of vowels
def vowel_count(str1):
    count=0
    for i in str1:
        if i in "aeiouAEIOU":
            count+=1
    return count
str2=input("enter the string:")
res=vowel_count(str2)
print("No of vowles = ",res)



# # # Q3.Define a function that takes length and breadth and returns area of
# # #rectangle
# def rectangle_area(l,b):
#     area=l*b
#     return area
# l=int(input("enter the length:"))
# b=int(input("enter the breadth:"))
# res=rectangle_area(l,b)
# print("Area = ",res)


# # # Q4.Define a function that takes a list of numbers and creates a new list
# # # with even numbers and returns the new list
# # l=[45,78,90,12,35]
# def even_list(l):
#     new=[i for i in l if i%2==0]
#     return new
# l=[45,78,90,12,35]
# new_list = even_list(l)
# print(new_list)

# #Q5.Define a function that takes list of 3 digit numbers and returns a new list where
# # each value is the sum of digits of corresponding number in the original list.
# l = [123, 345, 111, 678, 134, 809]

# def number_sum(l)+:
#     new=[]
#     for i in l:
#         sum=0
#         for j in str(i):
#             sum+=int(j)
#         new.append(sum)
#     return new
# l = [123, 345, 111, 678, 134, 809]
# new_list=number_sum(l)
# print(new_list)

