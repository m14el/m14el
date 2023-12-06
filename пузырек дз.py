from random import randint

arr = [randint(1, 100) for i in range(10)]
print(arr)
n = len(arr)
for i in range(n-1):
    is_sorted = True
    for j in range(n-1-i):
        if arr[j] > arr[j+1]:
            is_sorted = False
            arr[j], arr[j+1] = arr[j+1], arr[j]
    if is_sorted:
        break
print(arr)