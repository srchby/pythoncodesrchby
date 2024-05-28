class Student(object):
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def info(self):
    print(f"Name: {self.name}\nAge: {self.age}")

  def student(self):
    print("I'm a Student!")

class Teacher(Student):
  def __init__(self, name, age, subject):
    #The super class inherits from another class
    super().__init__(name, age)
    self.subject = subject

  #functions can be overridden
  def student(self):
    print("I'm not a Student!")

teacher1 = Teacher("Daniel", 32, subject="Mathematics")
student1 = Student("Michael", 16)

teacher1.info()
teacher1.student()
print("\n")
student1.info()
student1.student()