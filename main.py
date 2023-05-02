#2
import time


def time_function(func):
    def wrapper(*args, **kwargs):
        stat_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print('Час виконання функції', end_time - stat_time)
        return result
    return wrapper

@time_function
def example_function(x):
    time.sleep(1) #pass
    return x
print(example_function(666))

#1
urfyhrofgi '  u]' \
           '' \
           'ofjiogju' \
           'fhjehfuiewh' \
    dvfjrify
    oduue