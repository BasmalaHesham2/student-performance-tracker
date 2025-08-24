from utils import admin_only

class Gradebook:
    def __init__(self):
        self.students=[]
        self.subjects=[]
    @admin_only
    def addstudent(self,student):
        self.students.append(student)
    @admin_only
    def addsubj(self,subject):
        self.subjects.append(subject)

    def getstudent(self,id):
        for x in self.students:
            if id==x.getid():
                return x
        return None
    
    def assigngrade(self,id,subname,grade):
        student = self.getstudent(id)
        if(student):
            student.addgrade(subname,grade)
            print("grade assigned succssefully")
        else :
            print("Can't find student with this id")