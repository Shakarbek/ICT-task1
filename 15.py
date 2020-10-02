a=int(input())
f=[0,1]
n=2
while True:
    x=f[n-1]+f[n-2]
    f.append(x)
    if f[n]==a:
        print(n)
        break
    elif f[n]>a:
        print(-1)
        break
    n+=1
