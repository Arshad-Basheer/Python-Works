# l=[12,34,56,78,13,87,5]
# for i in l:
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         print(i,end=" ")
#
# l=[12,34,56,78,13,87,5]
# for i in l:
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i,end=" ")

for i in range(2,101):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=" ")