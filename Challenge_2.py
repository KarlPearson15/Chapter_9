#Challenge2.py
#Karl Pearson
#in collaboration with Karlos Calvillo and Thomas Morrissey
#3/5/2015

import random
RANKS = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"]
SUITS = ["c", "d", "h", "s"]
player1=0
player2=0
player1Name=input('Enter name: ')
player2Name=input('Enter name: ')
while player1 < 10 and player2 < 10:
    player1RankIndex=random.randrange(len(RANKS))
    player1Rank=RANKS(player1RankIndex)
    player1Suit=random.choice(SUITS)
    player1Card=player1Rank+player1Suit
    player2RankIndex=random.randrange(len(RANKS))
    player2Rank=RANKS(player2RankIndex)
    player2Suit=random.choice(SUITS)
    player2Card=player2Rank+player2Suit
    print(player1Name+':'+playerCard)
    print(player2Name+':'+playerCard)
    if player1RankIndex>player2RankIndex:
        print(player1Name, "has won this round and has gained 1 point.")
        player1 += 1
    elif player2RankIndex>player1RankIndex:
        print(player2Name, "has won this round and has gained 1 point.")
        player2 += 1
    else:
        print("Oh no, it's a tie!! No points awarded")
    print(Player1Name,":", player1)
    print(Player2Name,":", player2)
    input("Press enter for next round")
if player1=10:
    print(playre1Name," is victorious!")
else:
    print(playre2Name," is victorious!")
