s=input()
t=[]

for i in range(0,len(s)):
    t.append(s[i])

z=set(t)
print(len(z))

if len(z)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")