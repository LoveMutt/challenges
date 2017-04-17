from functools import wraps


def not_authorized(func_name, *args, **kwargs):
    print('You are not authorized for access to {} with args: {} and kwargs: {}'.format(func_name, args, kwargs))


def requires_authkey(func):
    """Decorator to check that a key is included in the kwargs as 'authkey'. If it is not present, a "not authorized"
    function is returned.
    """
    @wraps(func)  # preserves function meta data
    def wrapper(*args, **kwargs):
        # do stuff before func
        return func(*args, **kwargs)
        # do stuff after func
    return wrapper


@your_decorator
def some_function():
    pass


if __name__ == '__main__':
    some_function()
