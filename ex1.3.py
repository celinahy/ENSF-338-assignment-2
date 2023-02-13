storage = {}

def func(n):
    if n == 0 or n == 1:
        return n
    if n not in storage:
        storage[n] = func(n-1) + func(n-2)
    return storage[n]