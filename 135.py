def func(s):
    cnt={}
    for c in s:
        if c in cnt:
            cnt[c]= cnt[c]+1
        else:
            cnt[c]=1
    return cnt

str1=input()
str2=input()

cnt1=func(str1)
cnt2=func(str2)

if cnt1==cnt2:
    print("anagram")
else:
    print("Not anagram")