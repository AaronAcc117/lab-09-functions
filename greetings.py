def greet():
    print("Hello")

def say_hello_three_times():
    for i in range(3):
        greet()

say_hello_three_times()