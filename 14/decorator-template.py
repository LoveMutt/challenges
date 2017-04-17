from functools import wraps


def not_authorized(func_name, *args, **kwargs):
    print('You are not authorized for access to {} with args: {} and kwargs: {}'.format(func_name, args, kwargs))


def requires_authkey(func):
    """Decorator to check that a key is included in the kwargs as 'authkey'. If it is not present, a "not authorized"
    function is returned.
    """
    @wraps(func)  # preserves function meta data
    def wrapper(*args, **kwargs):
        if not kwargs:
            return not_authorized(func.__name__, *args, **kwargs)
        authkey = kwargs.get('authkey', None)
        if authkey is None:
            return not_authorized(func.__name__)
        return func(*args, **kwargs)
    return wrapper


@requires_authkey
def test_has_key(*args, **kwargs):
    print('Successfully read: args: {} and kwargs: {}'.format(args, kwargs))


if __name__ == '__main__':
    test_has_key(1, 2, 3, {'a': 1, 'b': 2})
    test_has_key(1, 2, {'a': 1, 'b': 2}, authkey='a')
