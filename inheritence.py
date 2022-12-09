#inheritence
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def printdetails(self):
        print(self.name,self.age)

person1 = person("John",30)

class student(person):
    def __init__(self,name,age,year):
        #person.__init__(self,name,age)
        super().__init__(name,age)
        self.admissionYear = year
    def greeting(self):
        print("Welcome","to the class of",self.admissionYear,self.name)
    # def printdetails(self):
    #     print(self.name,self,age,self.admissionYear)
student1 = student('peter',15,2022)
# print(student1.admissionYear)
student1.printdetails()
