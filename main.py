#Теорія Декоратори
#1
def my_decorator_func(func): #3
    def wrapper():
        print("Love you")
        func()
        print("I love")
    return wrapper

@my_decorator_func #2
def say_hello(): #1
    print("Hello!")
say_hello()
