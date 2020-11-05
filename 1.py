str=input()
s=str.lower()
for x in s:
    if x=="a" or x=="e" or x=="i" or x=="u" or x=="o" or x=="y":
        s=s.replace(x,"")
    # else:
    #     s[i-1]="."
t=""
for i in range(0, len(s)):
    t+="."
    t+=s[i]
print(t)