import random

currentStreak = 0
numberOfStreaks = 0
coinList = []

for experimentNumber in range(1000000):

    coin = ''

    if random.randint(0,1) == 0:
        coin = 'T'
    else:
        coin = 'H'

    if len(coinList) == 0:
        currentStreak += 1
        coinList.append(coin)
        continue
    elif coin == coinList[-1]:
        currentStreak += 1
    else:
        currentStreak = 0

    if currentStreak % 6 == 0 and currentStreak != 0:
        numberOfStreaks +=1

    coinList.append(coin)


print('Chance of streak: %s%%' % (numberOfStreaks / 10000))