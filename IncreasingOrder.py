n = int(input())
arr = list(map(int, input().split()))

max_num = max(arr)
tot = 0

for i in range(n):
    tot += max_num - arr[i]
print(tot)
    