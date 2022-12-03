class user:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printName(self):
        print(self.firstname,self.lastname)

user1=user("Jhon","Hop")

class student(user):
    def __init__(self, fname, lname):
        self.firstname = lname
        self.lastname = lname
    

student1=student("Peter","dom")
student1.printName()