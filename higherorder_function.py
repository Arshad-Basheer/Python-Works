#####MAP

# l=[1,2,3,4]
# print(list(map(lambda x:x**2,l)))
# print(list(map(lambda x:x**3,l)))
#
# #square root
# l=[25,36,81,100]
# print(list(map(lambda x:int(x**.5),l)))
#
# colors=['red','green','blue','yellow','black']
# new=list(map(lambda x:len(x),colors))
# print(new)
#
# #create a new list of first characters
# print(list(map(lambda x:x[0],colors)))
# #create a new list of last characters
# print(list(map(lambda x:x[-1],colors)))
# #create a new list of reverse of each elemnt
# print(list(map(lambda x:x[::-1],colors)))
# #Given a list
# l=[23,78,12,56]
# #Add 10 to each element in the given sequence
# print(list(map(lambda x:x+10,l)))
# ##given a list of dictionaries
# l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
#    {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
#    {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
# #
# # # create a new list of emails
# print(list(map(lambda x:x['email'],l)))



####FILTER

# #even
# l=[1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda x:x%2==0,l)))
#
# #value greater than 50
# l=[23,67,90,12,45,52]
# print(list(filter(lambda x:x>50,l)))
#
# #name whose length greater than
# f=['apple','orange','grapes','pineapple']
# print(list(filter(lambda x:len(x)>5,f)))
#
# #number divisible by 3 and 5
# l=[34,78,96,23,12,15]
# print(list(filter(lambda x:x%3==0 and x%5==0,l)))


####REDUCE

import functools

l=[1,2,3,4]
print(functools.reduce(lambda a,b:a+b,l,0))

print(functools.reduce(lambda a,b:a*b,l,1))


