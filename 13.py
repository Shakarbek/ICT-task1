arr=[]
while True:
    n=int(input())
    arr.append(n)
    if n==0:
        break
sum=0
for i in range(len(arr)):
    sum+=arr[i]
print(sum)