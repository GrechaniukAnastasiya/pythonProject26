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

#2
import time

def delay_decoraton(func):
    def wrapper(*args, **kwargs):
        time.sleep(3)
        return func(*args, **kwargs)
    return wrapper

@delay_decoraton
def sleepy():
    print('я сплю')
sleepy()
