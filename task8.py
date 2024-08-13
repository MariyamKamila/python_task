###  write a program to find the largest element in a  list

def largest_element (lst) :
    if  not lst:
        return None

    largest=lst[0]

    for element in lst:
        if element > largest:
            largest=element

    return largest

inputs =input("enter the number ")
number=list(map(int,inputs.split()))

if number:
    print("The largest element is:", largest_element(number))
else:
    print("No numbers were entered.")


### find the second largest element in a list:
user_input= input("enter the numbers :")
number=list(map(int,user_input.split()))
unique_number=list(set(number))
print("the entered number is :",unique_number)
number=sorted(set(number),reverse=True)
if len(number)>=2:
    print("The second largest element is :",number[1])
else:
    print("The list must have atleast two unique number")


### write a program that counts the number of words in a text

text= input("enter a text:")
word=text.split()
unique_word = list(set(word))
word_count=len(word)
print("the number of words in a text is :",word_count)
print("Unique words:",unique_word)

### write a  program to remove duplicate from a list

number=input("enter the number:")
unique_number=list(set(number))
print("the numbers are",number)
print("List after removing dublicate:",unique_number)


