from models.user import User

class Teacher(User):
    def __init__(self,username):
        super().__init__(username)
        self._role="Teacher"
    def displaydashboard(self):
        print(f"Welcome to teacher dashboard {self.username}")