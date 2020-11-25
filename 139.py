import random
n=15
def functions():
    card = {"B":[], "I":[], "N":[], "G":[] , "O":[]}
    lower = 1
    upper = 1 + 15
    for l in card:
        card[l] = random.sample(range(lower,upper), 5)
        lower = lower + n
        upper = upper + n
    return card


def displayCard(card):
    print("B   I   N   G   O")
    for letter in card:
        for number in card[letter]:
            print(number, end = "\t")
        print("\t")
    print("\t")

card = functions()
displayCard(card)

