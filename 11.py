n= int(input())
k=2
while k<=n:
    if n%k==0:
        break
    k+=1
print(k)