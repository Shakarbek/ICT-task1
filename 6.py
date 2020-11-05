s=input()
lower=0
upper=0

for t in s:
    if (t.islower())==True:
        lower+=1
    elif (t.isupper())==True:
        upper+=1

print(upper)
print(lower)

if lower>upper:
    s=s.lower()
elif upper>lower:
    s=s.upper()
else:
    s=s.lower()

print(s)