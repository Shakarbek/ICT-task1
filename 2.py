s=input()
t=""
for i in range(0, len(s)):
    if i%2==0:
        t+=s[i]

arr=list(t)
arr.sort()
print(arr)
t2=''
for char in arr:
        t2+=char
        t2+="+"

print(t2[:-1])
# for i in range(0, len(s)-2):
#     for j in range(0, len(s)):
#         j=i+2
#         if i%2==0:
#             if s[i]>s[j]:
#                 char=s[i]
#                 s[i]=s[j]
#                 s[j]=char
#
# print(s)

t1=sorted(t)
# print(t1)

