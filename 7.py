from string import ascii_lowercase

n=int(input())
s=input()
values=0

alphabet = list(ascii_lowercase)
diction=dict.fromkeys((char for char in alphabet), values)

# print(diction)
for char in s.lower():
    if char in diction.keys():
        diction[char]+=1

cnt=0
for num in diction.values():
    if num>0:
        cnt+=1

if cnt==26:
    print("YES")
else:
    print("NO")
print(diction)
