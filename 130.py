textLetters = {
    '1':['.', ',', '?', '!', ':'],
    '2':['A', 'B', 'C'],
    '3':['D', 'E', 'F'],
    '4':['G', 'H', 'I'],
    '5':['J', 'K', 'L'],
    '6':['M', 'N', 'O'],
    '7':['P', 'Q', 'R', 'S'],
    '8':['T' 'U' 'V'],
    '9':['W', 'X', 'Y', 'Z'],
    '0':[' ']
}

s=input()
s=s.upper()
s1=''
for c in s:
    for key, value in textLetters.items():
        if c in value:
            for a in range(value.index(c)+1):
                s1+=key

print(s1)