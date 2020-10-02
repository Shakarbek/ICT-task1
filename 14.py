arr=[]
while True:
    n=int(input())
    arr.append(n)
    if n==0:
        break
sum=0
maxi=max(arr)
print(maxi)
for i in range(len(arr)):
    if maxi==arr[i]:
        sum+=1
print(sum)