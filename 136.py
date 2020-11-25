from string import  punctuation
def func(s):
    cnt={}
    for c in s:
        if c in punctuation:
            continue
        if c in cnt:
            cnt[c]= cnt[c]+1
        else:
            cnt[c]=1
    return cnt

str1=input()
str2=input()

str1=(str1.lower()).replace(" ", "")
str2=(str2.lower()).replace(" ", "")

cnt1=func(str1)
cnt2=func(str2)

if cnt1==cnt2:
    print("anagram")
else:
    print("Not anagram")