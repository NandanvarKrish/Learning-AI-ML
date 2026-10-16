import numpy as np

def print_array(n, arr):
    if n >= len(arr):
        return
    print(arr[n])
    print_array(n+1, arr)


arr = [1,2,3,4,5]
print_array(0, arr)
