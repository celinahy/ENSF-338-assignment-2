import sys
import json
from time import perf_counter
import matplotlib.pyplot as plt


sys.setrecursionlimit(20000)


def func1(arr, low, high):
   if low < high:
       pi = func2(arr, low, high)
       func1(arr, low, pi-1)
       func1(arr, pi + 1, high)
def func2(array, start, end):
   p = array[start]
   low = start + 1
   high = end
   while True:
       while low <= high and array[high] >= p:
           high = high - 1
       while low <= high and array[low] <= p:
           low = low + 1
       if low <= high:
           array[low], array[high] = array[high], array[low]
       else:
           break
   array[start], array[high] = array[high], array[start]
   return high



with open("ex2.5.json", "r") as read_file:
   decodedData = json.load(read_file)


jsonSize = 0
for i in decodedData:
   jsonSize += 1

times = []
length = []
for j in range(jsonSize):


   length.append(len(decodedData[j]))
   t1 = perf_counter()
   func1(decodedData[j], 0, (len(decodedData[j]) - 1))
   t2 = perf_counter()


   finalTime = t2 - t1
   
   times.append(finalTime)


plt.scatter(length, times)
plt.title("Length of Array vs. QuickSort Algorithm Time")
plt.xlabel("Length of Array")
plt.ylabel("Time")
plt.show()
