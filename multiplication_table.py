while True:
    try:
        user_input = int(input("Enter a number to multiply :"))
        for i in range(1,11):
            print(f"{user_input}X{i} = {user_input*i}")
    except ValueError:
        print("Enter a Number")
