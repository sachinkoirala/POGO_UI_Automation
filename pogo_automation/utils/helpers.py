# utils/helpers.py
import random
import string

def generate_unique_id(length=16):
    return ''.join(random.choices(string.digits, k=length))