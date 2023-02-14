import timeit
from matplotlib import pyplot as plt

# timing original code
def original_func(n):
    if n == 0 or n == 1:
        return n
    else:
        return original_func(n-1) + original_func(n-2)

r = range(0, 36)
timer_data = []
for i in r:
    elapsed_time = timeit.timeit(lambda : original_func(i), number=1)
    timer_data.append(elapsed_time)
plt.plot(r, timer_data)
plt.show()

# timing optimized code
storage = {}

def func(n):
    if n == 0 or n == 1:
        return n
    if n not in storage:
        storage[n] = func(n-1) + func(n-2)
    return storage[n]

r2 = range(0, 36)
timer_data2 = []
for i in r2:
    elapsed_time2 = timeit.timeit(lambda : func(i), number=1)
    timer_data2.append(elapsed_time2)
    storage.clear()
plt.plot(r2, timer_data2)
plt.show()
