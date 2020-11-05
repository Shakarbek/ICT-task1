n=int(input())
s=input()
a_cnt=0
d_cnt=0
for char in s:
    if char=="A":
        a_cnt+=1
    elif char=="D":
        d_cnt+=1

if a_cnt>d_cnt:
    print("Anton")
elif d_cnt>a_cnt:
    print("Danik")
else:
    print("Friendship")