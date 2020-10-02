# pool minimum distance to the side
n=int(input())
m=int(input())
x=int(input())
y=int(input())

distance=min(n-x, x, m-y, y)
print(distance)