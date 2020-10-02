import array
n=int(input())
m=1
k =int()
my_arr= []
while n>k:
    k=m*m
    if k<n:
        my_arr.append(k)
        # print(k)
    m+=1
# print(my_arr)

for i in my_arr:
    print(i, ' ')