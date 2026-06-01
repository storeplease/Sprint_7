import random

class TestHelper:
    @staticmethod
    def generate_random_string(length=10):
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        return ''.join(random.choice(letters) for _ in range(length))   