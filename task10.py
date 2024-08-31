## 1.Write a function that calculates the average of a list of numbers

def average_calculate (numbers):
    if len(numbers)==0:
        return 0, 0, 0
    else :
        total_sum=sum(numbers)
        length=len(numbers)
        average_sum =total_sum /length
        return total_sum,length,average_sum


numbers_input = input("Enter numbers separated by spaces: ")
numbers = list(map(float, numbers_input.split()))
total_sum ,length ,average_sum =average_calculate(numbers)
print("the total sum is:{}".format(total_sum))
print("the total length is:{}".format(length))
print("The average is: {:.2f}".format(average_sum))

#2.Write a function that returns the sum of digits of a given number


def sum_and_length(number1):
    if len(number1)==0:
        return 0 , 0
    else:
        total_sums= sum(number1)
        length_1=len(number1)
        return total_sums , length_1

print("RETURN THE SUM OF DIGITS:")
number_input=input("enter the numbers separated by spaces:")
number1=list(map(float,number_input.split()))
total_sums , length_1= sum_and_length(number1)
print("the length of the digits is:",length_1)
print("the total sum of digits is:",total_sums)

### 3.Write a function that checks if a given number is prime.

def Is_prime(number11):
    if number11<2:
        print(f"{number11} is not a prime number because the number is less than 2")

    for i in range(2,int(number11**0.5)+1):
        if number11 % i == 0:
            print(f"{number11} is not a prime because it is divisible by {i}")
            return
    print(f"{number11} is a prime number")

number11 =int(input("enter the number"))
Is_prime(number11)





