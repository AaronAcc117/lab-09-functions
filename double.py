def double(n): #function
    return n * 2

def calculate_double():
    user_input = input("Enter a number to double: ")
    number_to_double = int(user_input)
    result = double(number_to_double)
    print(result)

calculate_double()