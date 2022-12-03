#create a class create an object, __ini__() function, objects method,self parameters.
# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# obj=person("Jhon",20)

# obj.age = 30 modify the object paramerters
# print(obj.age)
# del obj.age
# print(obj.age)
# del obj
# print(obj)()
# print(obj.name)

class user:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
    def printName(self):
        print(self.firstname,self.lastname)

user1=user("Jhon","Hopkins")
print(user1.firstname)
print(user1.lastname)
print(user1.firstname,user1.lastname) #tuple type
print(user1.firstname+" "+user1.lastname) #string type


#inheritence
'''parent class(base class) 
and child class(derived class)
user class-> student, programmer, teacher some common property like name

'''
class student(user):
    pass

student1=student("Mike", "Tyson")
print()
