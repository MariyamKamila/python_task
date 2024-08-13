### 1. Develop a program that stimulate a game of rolling a dice.
# Roll the dice until you get a 6 and count the number of rolls it take to get a 6 .
# print the count using a break statement.

import random
def roll_dice():
    return random.randint(1,6)

def roll_until_six():
    count=0

    while True:
        count=count+1
        dice_result = roll_dice()
        print("The rolled dice is {}".format(dice_result))

        if dice_result ==6:
            print("To get 6 it took {} rolls".format(count))
            break
roll_until_six()

### 2. Create a class Teacher with name ,age and salary attribute
# where salary must be private attribute and cannot be accessed outside the class

class Teacher:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.__salary=salary

    def get_salary(self):
        return self.__salary

    def set_salary(self,new_salary):

        if new_salary >0:
            self.__salary=new_salary
        else:
            print("salary must be positive")
name=input("Enter the Teacher's name :")
age=input("Enter the Teacher's age")
salary=input("Enter the Teachers salary:")

teacher=Teacher(name,age,salary)

print("\n Teachers details")
print("Name is:",teacher.name)
print("Age is:",teacher.age)
print("Salary is:",teacher.get_salary())


### 3.write a python program to create a person class.
# Include attribute like name,country and date of birth.
# Implement a method to determine the persons age
import datetime
class Person :
    def __init__(self,name,country,dob):
        self.name=name
        self.country=country
        self.dob=datetime.strptime(dob,"%y-%m-%d")

    def person_age(self):
        today=datetime.today()
        age = today.year - self.dob.year
        if (today.month, today.day) < (self.dob.month, self.dob.day):
            age -= 1
        return age
name=input("Enter the name:")
country=input("Enter the country:")
dob=("Enter the date of birth(YYYY-MM-DD:")

person = Person(name, country, dob)

print("\nName: {person.name}")
print(f"Country: {person.country}")
print(f"Date of Birth: {person.dob.strftime('%Y-%m-%d')}")
print(f"Age: {person.get_age()} years old")


