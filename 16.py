arr=[]
while True:
    n=int(input())
    arr.append(n)
    if n==0:
        break
sum=0
for i in range(arr[0], len(arr)-1):
    if arr[i]>arr[i+1] and arr[i]>arr[i-1]:
        sum+=1
print(sum)