list=[1,2,3]
print(list)
print(type(list))

#index  0  1  2  3   4       5
list1=[11,12,13,14,'Chair','car']
print(list1)
print(type(list1))

print(list1[1])
print(list1[5])

list2=[11,12,13,14,False,'Pencil']
print(list2)



#access iteams
listOne=[10,20,30,40,50,60,70]
print(listOne[0:5])
print(listOne[:6])
print(listOne[5:])

#Modify list 
listOne[0]=13
listOne[5]='Python'
print(listOne) 

#Change a range of list iteams
listOne[0:4]=['Java','C++']
print(listOne) 

 

#insert() iteams
listX=[1,2,3,4,5]
listX.insert(2,6)
print(listX)


#append()
listX.append(7)
listX.append(8)
listX.append('Mysql')
print(listX)


# extend()
listY=[11,13,17]
listX.extend(listY)
print(listX)

tup=(19,21)
listX.extend(tup)
print(listX)



#remove()
mylist = ['Ajay','Rohit','Karan']
mylist.remove('Rohit')
print(mylist)



#pop()
mylist = ['Ajay','Rohit','Karan','Akash']
mylist.pop(3)
print(mylist)

del mylist[1]
print(mylist)


