class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        return("I am {name}, I'm {age} years old".format(name = self.name, age = self.age))

class Employee(Person):
    def __init__(self, name, age, job):
        super().__init__(name, age)
        self.job = job

    def introduction(self):
        print("{hello} and I work as {job}".format(job = self.job, hello = self.hello()))
        #print("Hello, I'm {name}, I'm {age} and I work as a {job}".format(name = self.name, age = self.age, job = self.job))

    def helloThere(self):
        print(self.hello())
"""
jun = Person("Jun", 17)
jun.hello()
"""
bob = Employee("bob", 20, "programmer")
bob.hello()
bob.introduction()
bob.helloThere()