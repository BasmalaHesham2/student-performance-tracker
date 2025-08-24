_current_user = None

def set_current_user(user):
    global _current_user
    _current_user = user

def get_current_user():
    return _current_user


def admin_only(func):
    def wrapper(self,*args,**kwargs):
        if getattr(self,"current_user",None) and self.current_user._role!="Admin":
            print("Access denied admins only")
        return func(self,*args,**kwargs)
    return wrapper

def log_action(func):
    def wrapper(*args,**kwargs):
        print(f"LOG : {func.__name__} was called")
        return func(*args,**kwargs)
    return wrapper
