n=int(input())
arr=[]

while len(arr)<n:
    x = input();
    arr.append(x);

def func(arr, n):
    sum = 0;
    arr.sort();
    i = 0;

    while i < (n - 1):
        if (arr[i] == arr[i + 1]):
            sum+=1;
            i=i+2;
        else:
            i+=1;
    return sum;

print(func(arr, n));