# *
# * *
# * * *
# * * * *
# * * * * *
# n=int(input("Enter the value:"))
# for i in range(1,n+1):
#     for j in range(i):
#         print(i,end=" ")
#     print()

# * * * * *
# * * * * 
# * * * 
# * * 
# * 

# a=int(input("Enter the value :"))
# for i in range(5,0,-1):
#     for j in range(i):
#         print(i,end=" ")
#     print()

#     *
#    * *
#   * * *
#  * * * *


# b=int(input("Enter the value Triangle:"))
# for i in range(1,b+1):
#     for j in range(b-i):
#         print(" ",end="")
#     for j in range(i):
#         print("* ",end=" ")
#     print()

'''

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*

'''

n=int(input("Enter the value of for this pattern"))
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()

for l in range(n-1,0,-1):
    for k in range(l):
        print(l,end=" ")
    print()
    