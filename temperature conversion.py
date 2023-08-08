unit = input("Please Enter the Unit of Temperature (Celcius/Fahrenheit) : ")
temp_unit = float(input("Enter the Temperature : "))

if unit == "Celcius":
    temp = (temp_unit *(9/5)) + 32
    print("Temperature is ", (temp))
elif unit == "Fahrenheit":
    temp = (temp_unit - 32) * (5/9)
    print("Temperature is ",(temp))
else:
    print("Unit is in Invalid Format. Please Enter Celcius or Fahrenheit")