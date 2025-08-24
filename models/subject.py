class Subject:
    def __init__(self,name,code):
        self.name=name
        self.code=code
    def __str__(self):
        return f"{self.code} - {self.name}"
    
        