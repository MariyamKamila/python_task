 ### 1.Develop the program that ask the user for number until they enter 0
 # print the sum of all the numbers entered by the user
 # except for the number 7 using the contiue statemenet to skip

sum=0
skip=[]
while True:
      number= float(input("Enter the number:"))
      if number<1:
          print("Oops! you have entered zero ....Bye bye")
          break
      if number==7:
          skip.append(number)
          continue
      sum=sum+ number
print("the total value is={}".format(sum))
print("the skipped value is ={}".format(skip))


### 2. create the program to generate the random number between 1 and 100
 # untill they generate a number that is a perfect square.
 # print the number and square root then terminate the loop using the break statement

import random

while True:
    num=random.randint(1,100)
    print("the random number is:",num)

    sqrt_num=num**0.5
    if int(sqrt_num)==sqrt_num:
        print("the perfect square is {} and the number is {}".format(num,sqrt_num))
        break

### 3. write a program to print all the vowels in a given string
 # but skip printing if the character is a space using a continue statement

text= input("enter the string:")
for char in text:
    if char==" ":
        continue
    if char.lower() in "aeiou":
        print(char)
print("The User text is :",text)