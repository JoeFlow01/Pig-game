import random

player1_total = 0
player2_total = 0

t1 = 'y'
t2 = 'y'

player1_subtotal = 0
player2_subtotal = 0

playing = True

while playing:

    print("player 1 turn")

    while t1 == 'y' and playing:
        roll = random.randint(1, 6)
        print("player1 got: ", roll)
        if roll == 1:
            print("bad luck bro")
            player1_subtotal = 0
            t1 = 'h'
            print("player1 current score", player1_total)
        else:
            player1_subtotal += roll
            print("player1 current score", player1_total, "player1 current subtotal score", player1_subtotal)
            turn = input("type y to continue or h to hold")
            if turn == 'h':
                player1_total += player1_subtotal
                t1 = 'h'
                player1_subtotal = 0
                print("player1 current score", player1_total)
    if player1_total >= 100:
        print("player 1 won with score:", player1_total, "and player 2 score:", player2_total)
        playing = False
        break

    t1 = 'y'
    print("player 2 turn")

    while t2 == 'y' and playing:
        roll = random.randint(1, 6)
        print("player2 got: ", roll)
        if roll == 1:
            print("bad luck bro")
            player2_subtotal = 0
            t2 = 'h'
            print("player2 current score", player2_total)
        else:
            player2_subtotal += roll
            print("player2 current score", player2_total, "player2 current subtotal score", player2_subtotal)
            turn = input("type y to continue or h to hold")
            if turn == 'h':
                player2_total += player2_subtotal
                t2 = 'h'
                player2_subtotal = 0
                print("player2 current score", player2_total)
    if player2_total >= 100:
        print("player 2 won with score:", player2_total, "and player 1 score:", player1_total)
        playing = False
        break

    t2 = 'y'
