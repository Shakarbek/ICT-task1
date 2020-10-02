n=int(input())
arr=[]
while len(arr)<n:
    x=int(input())
    arr.append(x)
sum=0
list=[]
for i in range(0, len(arr)):
    if i==0:
        print(arr[-1], ' ')
    else:
        print(arr[i-1], ' ')

