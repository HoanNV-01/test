class Person:
   def __init__(self, name: {str}, age: {int}):
        self.name = name
        self.age = age
   def myfunc(self):
        print("Hello my name is " + self.name)
        print("I am " + self.age + " years old")

Person1 = Person("John", "36")
Person1.myfunc()

