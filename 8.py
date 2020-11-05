s=input()
t=input()

if s==t[::-1]:
    print("YES")
else:
    print("NO")
# k1=[]
# v1=[]
# for char in s:
#     k1.append(char)
#     v1.append(s.index(char))
# d1=dict(zip(k1,v1))
#

# k2=[]
# v2=[]
# for char in t:
#     k2.append(char)
#     v2.append(len(t)-1-t.index(char))
# d2=dict(zip(k2,v2))
# print(d1)
# print(d2)
#
# if len(s)!=len(t):
#     print("NO")
# elif d1==d2:
#     print("YES")
# else:
#     print("NO")
