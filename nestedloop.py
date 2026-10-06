# l=['kelly','emy','alan']
# for i in l:
#     for j in range(3):
#         print(i,end=" ")
#     print()

# l=[1,2,3]
# no=['what','when','why']
# for i in l:
#     print(i,":",end=" ")
#     for j in no:
#         print(j)
#         print("    ",end='')
#     print()
#

l=[{'id':101,'name':'arun','age':23},
   {'id':102,'name':'amal','age':24},
   {'id':103,'name':'anu','age':22}]

for i in l:
    for j in i.values():
        print(j,end=" ")
    print()