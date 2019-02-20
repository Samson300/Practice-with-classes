# name
# avatar : (Profile picture)
# inventory

class Character():
    def __init__(self, new_name, new_avatar):
        self.name = new_name
        self.avatar = new_avatar
        self.inventory = []
    def greet(self, someone=None):
        # When we assume that "someone" argument has a ".name" property
        # this is an object-oriented programing principle called
        # polymorphism.
        # in Python, its called "Duck Typing"
        if someone is not None:
            return "Hello, %s, I am %s. I am awesome." % (someone.name, self.name,)
        else:
            return "Hello, I am %s. I am awesome." % (self.name,)