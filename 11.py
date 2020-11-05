n=int(input())
s=input()
t=""
for char in s:
    if char=="z":
        t+='0 '
    elif char=='n':
        t+='1 '

print(t)