from random import randrange
rolls = 1000


def twoDice():
    d1 = randrange(1, 7)
    d2 = randrange(1, 7)
    return d1 + d2

expectedDict = {
    2:1/36, 3:2/36, 4:3/36, 5:4/36, 6:5/36, \
    7:6/36, 8:5/36, 9:4/36, 10:3/36, 11:2/36, \
    12:1/36}

countDict = {
    2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}

for i in range(rolls):
    t = twoDice()
    countDict[t] = countDict[t] + 1

print("Total    Simulated   Expected")
print("          Percent    Percent")


for i in sorted(countDict.keys()):
    print("%4d  %11.2f   %8.2f" %\
          (i, countDict[i] / rolls * 100, expectedDict[i] * 100))