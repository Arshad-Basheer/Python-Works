# # # #create a new list with square root of each element
# l=[25,16,9,36]
# l1=[int(i**.5) for i in l]
# print(l1)


# # #Given a dictionary
# d={'arun':25,'amal':34,'akhil':26,'anu':21}
# # # create a list of names
# # # create a list of marks
# l1=[i for i in d]
# print(l1)
# l2=[i for i in d.values()]
# print(l2)
#


# # #Given a list
# l=[23,56,12,89,-34,-23,-67,-43,9.7,4.5,'hello','world']
# # #create a list of string values
# # #create a list of floats
# # #create a list of positive numbers
# l1=[i for i in l if type(i)==str]
# print(l1)
# l2=[i for i in l if type(i)==float]
# print(l2)
# l3=[i for i in l if (type(i)==int or type(i)==float) and i>0]
# print(l3)


# #
# #
# # #Given a list
# fruits=['apple','orange','pineapple','avocado','grapes']
# # #create a new list with elements whose length is greater than 6
# l=[i for i in fruits if len(i)>6]
# print(l)

# #
# # # #create a new list with elements whose value is divisible by 3 in range(1,101)
# # l=[i for i in range(1,101) if i%3==0]
# # print(l)
# # Given
# s="python coding  is easy and fun"
# # # create a new list with only vowels
# l=[i for i in s if i.upper() in "AEIOU"]
# print(l)


# ##SET COMPREHENSION
# s="python coding is easy and fun"
# new={i for i in s if i!=" "}
# print(new)
#
# new={i for i in s if i.upper() in "AEIOU"}
# print(new)
#
# new=[len(i) for i in s.split()]
# print(new)

#DICTIONARY COMPREHENSION
l=[10,20,30,40]
# new={i:i**2 for i in l}
# print(new)

new={i:l[i] for i in range(len(l))}
print(new)

s="python coding is easy and fun"
new={i:len(i) for i in s.split()}
print(new)