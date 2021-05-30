def decorator_function(any_func):
    def wrapper_function():
        print('This is how we add more functionalities using decorators')
        any_func()

    return wrapper_function


@decorator_function  # this is shortcut
def fun():
    print('this is function. and we don\'t want to change it')


fun()

# var = decorator_function(fun)
# var()

# fun = decorator_function(fun)       #we can also use function name as decorators
# fun()
