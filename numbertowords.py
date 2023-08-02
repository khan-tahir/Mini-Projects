from num2words import num2words

num = int(input("Enter the number to convert it into word : "))

numtoword = num2words(num)

print(f"Entered number {num} in words is {numtoword}")