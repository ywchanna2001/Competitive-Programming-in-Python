arr = list(map(int, input().split()))
n = len(arr) 
tot_trans=0

trans = [1] * n
for i in range(1,n):
    if(arr[i] > arr[i-1]):
        trans[i] = trans[i-1] + 1

for j in range(n-1, -1, -1):
    if(arr[j-1]> arr[j]):
        trans[j-1] = trans[j] + 1
    tot_trans += trans[j]
    
print(tot_trans)
