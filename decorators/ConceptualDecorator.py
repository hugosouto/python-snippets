def decorator(function):
    def wrapper():
        print("I'm before the execution of the function passed as an argument")
        function()
        print("I'm after the execution of the function passed as an argument")
    return wrapper

def another_function():
    print("I'm a beautiful argument!")

decorated_function = decorator(another_function)
decorated_function()