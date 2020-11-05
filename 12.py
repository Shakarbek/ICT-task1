n=int(input())
s=input()
cnt=0
b=False
for i in range(0, len(s)-2):
    if s[i]=="x" and s[i+1]=="x" and s[i+2]=="x":
        cnt+=1

if cnt==0:
    print(0)
else:
    print(cnt)