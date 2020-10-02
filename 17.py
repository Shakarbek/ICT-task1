n=int(input())
arr=[]
while len(arr)<n:
    x=int(input())
    arr.append(x)
sum=0
list=[]
for i in range(arr[0], len(arr)-1):
    if arr[i]==arr[i+1]:
        sum+=1
print(sum)