## 1. write a program to print all the even number between 1 and 20,
# skipping the number 10 using a continue statement

for number in range(1 , 21):
    if number % 2==0 :
        continue
    if number ==10:
        continue
    print (number)


### 2 . create a program that ask the user for numbers until they enter a negative number .
# Print the sum of all the positive number entered by the user,
# terminate the loop when a negative number is entered using a break statement.
sum=0;
while True:
    number = float(input("Enter a number :"))
    if number < 0:
        print("You have entered the negative number.Exiting the program")
        break
    sum=sum+number
print(f"You entered: {number}")
print(f"the total sum is :{sum}")

### 3. writ a program to find the first 5 multiples of 3,
## but if a multiple of 3 is divisible by 5 skip it using a continue statement
skipped=[]
for i in range( 1,11):
    if i==6 :
        break
    result=i*3
    if result % 4==0:
        skipped.append(result)
        continue
    print("3 *{} ={}".format(i,result))
print("the number divisble by 4 ={} ".format(skipped))
