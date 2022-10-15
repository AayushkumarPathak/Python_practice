#List sorting

#sort in alpha numeric order default it is ascending.

'''my_list=['banana','apple','gauava','orange']
s=my_list.sort()
print(my_list) 
s=my_list.sort(reverse=True)
print(my_list) 

my_list=[90,400,500,678,56,150]
my_list.sort()
print(my_list)

#For descending order .sort(reverse=True)
my_list.sort(reverse=True)
print(my_list)'''

'''case Sensitive'''
'''my_list=['banana','Apple','gauava','Orange']
my_list.sort(key = str.lower)
print(my_list)'''

'''reverse'''
'''my_list.reverse()
print(my_list)'''

list1=[10,20,30,40]
list2=list1
list2=list(list1) #another way to copy list.
print(list2)
list2.pop()
print(list1)
print(list2)