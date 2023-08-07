#Finding Factorial Using Recursion
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return (num*factorial(num-1))
    
user_input = int(input("Enter a number to find it's factorial : "))
print(factorial(user_input))
