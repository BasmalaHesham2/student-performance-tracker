from abc import ABC,abstractmethod

class User(ABC):
    
    def __init__(self,username):
        self.username=username
        self._role="user"
    @abstractmethod
    def displaydashboard(self):
        pass

