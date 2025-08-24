from models.user import User

class Admin(User):
    def __init__(self,username):
        super().__init__(username)
        self._role="Admin"
    def displaydashboard(self):
        print( f"Admin dashboard welcome {self.username}" )
    
    