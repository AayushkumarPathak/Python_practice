#for loop
num=[10,20,30,40]
for x in num:
    print(x)
print("---------------")
""" for x in "hello":
    print(x)  """

num=[10,20,30,40,50]
for x in num:
    print(x)
    if(x==30):
        break
print("---------------")
for x in num:
    
    if(x==30):
        break
    print(x)

print("---------------")
for x in range(6):
    print(x)
print("---------------")
for x in range(2,10,2):
    print(x)

print("---------------")

for x in range(5):
    print(x)
else:
    print("Finally the process is finished")

print("---------------")
for i in range(5):
    if i==3: break
    print(i)
else:
    print("The process is finished")
print("---------------")
arr1=[1,2]
arr2=[5,6]
for x in arr1:
    for y in arr2:
        print(x,y)

#inner loops gets executed once for each iteration of the outer loop.
for x in[10,20,30]:
    pass
print("hello")