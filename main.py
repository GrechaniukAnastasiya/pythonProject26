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

#3

def chache_decoraton(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n], cache
    return wrapper

@chache_decoraton
def fibonacci(n):
    if n in(0,1):
        return n
    return fibonacci(n-1) + fibonacci(n - 2)
print(fibonacci(10))

