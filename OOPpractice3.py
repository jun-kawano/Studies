names = []
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        names.append(self.name)

    def hello(self):
        print("I am {name} and I'm {age} years old".format(name = self.name, age = self.age))
        return ("I am {name} and I'm {age} years old".format(name = self.name, age = self.age))

    @classmethod
    def number_people(cls):
        return len(names)
    
    @classmethod
    def name_people(cls):
        return names

class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school
    def hello_there(self):
        self.hello()
        print(" and I study at {self.school}")

p1 = Person("Jun", 17)
p2 = Person("Giulia", 17)
p3 = Person("Sofia", 17)
p4 = Person("Gustavo", 17)
p5 = Person("Enzo", 18)
people = [p1, p2, p3, p4, p5]

#for person in people:
#    person.hello()

p1 = Student("Jun", 17, "ufsc")
p1.hello_there()

#print(f"There are {Person.number_people()} people")
#print(Student.name_people())