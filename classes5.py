class Person:


    def __init__(self, lname,fname,dob):
        self.lname = lname
        self.fname = fname
        self.dob = dob
        
    def student(self,ID,grades):
        self.ID = ID
        self.grades = grades
        #grades = 0


studentInfo = Person("Nestor","Rivas","05/29/1981")
grades = Person.student(101,99)

print(studentInfo.lname,studentInfo.fname,studentInfo.dob)
print(studentInfo.grades)

