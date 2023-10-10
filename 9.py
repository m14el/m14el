x = int(input())
count = 0
n = 1
while n * n < x:
    if x % n == 0:
        count += 2
    n += 1
if x%n==n:
    count += 1
print(count)