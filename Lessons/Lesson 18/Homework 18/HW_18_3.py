# Write a class TypeDecorators which has several methods for converting results of functions to a specified type
# (if it's possible):

from functools import wraps


class TypeDecorators:

    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args):
                result = func(*args)
            try:
                return int(result)
            except ValueError:
                print('Convertion is not possible')
                return result
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args):
            result = func(*args)
            try:
                return str(result)
            except ValueError:
                print('Convertion is not possible')
                return result
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args):
            result = func(*args)
            try:
                return bool(result)
            except ValueError:
                print('Convertion is not possible')
                return result
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args):
            result = func(*args)
            try:
                return float(result)
            except ValueError:
                print('Convertion is not possible')
                return result
        return wrapper