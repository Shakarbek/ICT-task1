s=input()
one=0
zero=0

for i in range(0, len(s)):
    if s[i]=="1":
        one+=1
        zero=0
    else:
        zero+=1
        one=0
    if zero==7 or one==7:
        break

if zero==7 or one==7:
    print("YES")
else:print("NO")