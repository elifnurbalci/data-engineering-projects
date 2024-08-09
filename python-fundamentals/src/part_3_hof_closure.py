def generate_multiples(multi):
    def mults(length):
        if length == 0:
            return []
        elif length == 1:
            return [multi]
        elif length > 1:
            return [multi*i for i in range(1,length+1)]
    return mults


def secure_func(password):
    def decorator(func):
        def wrapper(*args, **kwargs):
            user_input = input('What is the password? ')
            if user_input == password:
                return func(*args, **kwargs)
            else:
                return "Sorry your password is incorrect!"
        return wrapper
    return decorator


@secure_func("nc123@!")
def say_secret():
    return "Hopscotch"

@secure_func("nc123@!")
def sum(a,b):
    return a+b