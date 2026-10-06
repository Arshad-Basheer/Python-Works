# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# for i in range(4,1,-1):
#     for j in range(1,i):
#         print("*",end=" ")
#     print()

# k=3
# for i in range(1,4):
#     for k in range(1,k+1):
#         print(" ",end=" ")
#     k-=1
#     for j in range(1,i+1):
#         print("*",end="   ")
#     print()
# k=0
# for i in range(5,1,-1):
#     for k in range(1,k+1):
#         print("",end=" ")
#     k+=2
#     for j in range(1,i):
#         print("*",end="   ")
#     print()

k=3
for i in range(2,9,2):
    for d in range(2):
        for p in range(1,k+1):
            print("  ",end=" ")
        for j in range(1,i+1):
            print("*",end="  ")
        print()
    k-=1
    # for c in range(1,a+1):
    #     print("  ",end=" ")
    # a-=1
    # for j in range(1,i+1):
    #     print("*",end="  ")
    # print()