n= int(input())
k=int(input())

list=[]
for i in range(k):
    l=int(input())
    r=int(input())
    # if i<l:
    #     list[i]='|'
    # elif i>=l and i<=r:
    #     print('. ')
    # elif i>r:
    #     print('| ')


for i in range(n):
    if i<l:
        print('| ')
    elif i>=l and i<=r:
        print('. ')
    elif i>r:
        print('| ')