# name
# avatar : (Profile picture)
# inventory

class Character():
    def __init__(self, new_name, new_avatar):
        self.name = new_name
        self.avatar = new_avatar
        self.inventory = []
    def greet(self, someone=None):
        if someone is not None:
            return "Hello, %s, I am %s. I am awesome." % (someone.name, self.name,)
        else:
            return "Hello, I am %s. I am awesome." % (self.name,)