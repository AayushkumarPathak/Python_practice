#Tuple datatype
'''-->tuple is ordered 
-->Used to store multiple items in a single variable
-->Tuples cannot be duplicated
-->Tuples are immutable datatype i.e unchangeable
-->They are written eith round brackets'''

my_tuple=(10,20,30,40)
#my_tuple[1]=100 wrong !
print(my_tuple)
print(len(my_tuple))

#create a tuple with one iteam ,always add after the iteam
myTuple=(10,)
print(myTuple)

myTuple=(10,'apple',20)
print(myTuple)
#tuple constructor
myTuple=tuple((10,20,30,40))
print(myTuple[2:4])

print(myTuple[-3:-1])

#Immutable --> mutable
newTuple=(10,20,30,40)
list1=list(newTuple)
print(list1)
list1[2]=200
print(list1)

#append tuple with another tuple

tuple2=(10,20,30,40)
x=(50,)
tuple2=
