class person:

    def __init__(self):
     self.age = 0

    def getter(self):
        return self.age

    def setter(self,a):
      a=input("enter the age")     
      self.age = a

waleed = person()

print("the age is",waleed.age)      