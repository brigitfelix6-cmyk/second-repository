# class student:
#     student_name="millie"
#     gender="female"
#     admission_number=1234
# def student_details(self):
#     print(self.student_name)
#     print(self.gender)
#     print(self.admission_number)
class Animal:
    name="rohu"
    color="black"
    age=3
    def eat(self):
        print("i can eat")
class Dog(Animal):
    def display_name(self):
        print(self.name)
    def display_color(self):
        print(self.color)
Animal1=Dog()
print(Animal1.name)
print(Animal1.color)
print(Animal1.age)
