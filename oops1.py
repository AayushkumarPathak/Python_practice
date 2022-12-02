class Myclass:
    a=40
object=Myclass()
object2=Myclass()
print(object.a,object2.a)


# print(Myclass)
#__init__() - all classes have this prebuilt function which is 
#             alwaysnexecueted when the class is being executed

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(name,age)
person1=person("Jhon",40)
person2=person("Peter",20)
print(person1.name)
print(person2.name)

#user defined function in classes;
#object method

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(name,age)
    
    def myfunc(self):
        print("My name is " + self.name)
person1=Person("Jhon",40)
person2=Person("Peter",20)
person1.myfunc()
person2.myfunc()
#the referance to the current instance of the class will always be the
#first parameter to the fun that u define inside the clas