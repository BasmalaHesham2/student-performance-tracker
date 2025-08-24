class Student:
    def __init__(self,id,name):
        self.__id=id
        self.__name=name
        self.__grade={}
    def addgrade(self,subject,grade):
        self.__grade[subject]=grade
    def calcGPA(self):
        if not self.__grade:
            return 0.0
        return sum(self.__grade.values()) / len(self.__grade)
    def getreport(self):
        print(f"student : {self.__name} Report :")
        print(f"GPA: {self.calcGPA()}")
        for subject,grade in self.__grade.items():
            print(f"{subject} : {grade}")
    
    def getid(self):
        return self.__id
    def getname(self):
        return self.__name

        