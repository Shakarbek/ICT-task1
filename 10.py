s=input()
t=False
if s.isupper():
    t=True
    print(s[0]+s[1:].lower())
elif s[0].islower() and s[1:].isupper():
    print(s[0].upper() + s[1:].lower())
else:
    print(s)