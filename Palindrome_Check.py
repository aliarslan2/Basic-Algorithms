"""
Created on Sat Aug  5 19:13:14 2023

"""
def palindrome1(number1):
    reverseNumber=0
    
    num =number1
    i=0
    while num>=10:
        i+=1
        num=num//10
        
    return i

def palindrome2(number1,i):
    reverseNumber=0
    str1=""
    
    num = number1
    while i>=1:
        multiplier1=10**i
             
        i-=1
        
        multiplier2=num%10
        str1+=str(multiplier2)
        
        num=num//10
        
        reverseNumber+=multiplier1*multiplier2

    return str1

number=str(input("Enter your number: "))
number1=int(number)

i=palindrome1(number1)+1

Reverse_of_the_number =palindrome2(number1,i)

k=0
while number[k]==str(0):
    k+=1
    Reverse_of_the_number+=str(0)


print("Reverse of the number: ",Reverse_of_the_number)
    
if (number==Reverse_of_the_number):

    
    print("Our number is a palindrome number. ")
else:
    print("Our number is not a palindrome number!!! ")


