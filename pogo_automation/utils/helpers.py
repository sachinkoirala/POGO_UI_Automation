# utils/helpers.py
import random
import string

def generate_unique_id(length=12):
    return ''.join(random.choices(string.digits, k=length))

def generate_screenname(prefix_length=1, id_length=16):
    prefix = ''.join(random.choices(string.ascii_letters, k=prefix_length))
    unique_id = generate_unique_id(id_length)
    return prefix + unique_id