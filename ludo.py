import random

position1 = 0
position2 = 0
position3 = 0
position4 = 0



while True:
    
    #PLAYER 1:
    
    input("Player 1: Press Enter to roll the dice...")
    dice = random.randint(1, 6)
    print("Player 1 rolled:", dice)
    position1 += dice

    if position1 >= 50:
        
        print("Player 1 Wins!")
        break

    print("Player 1 Position:", position1)

    #PLAYER 2:

    input("Player 2: Press Enter to roll the dice...")
    dice = random.randint(1, 6)
    print("Player 2 rolled:", dice)
    position2 += dice

    if position2 >= 50:
        print("Player 2 Wins!")
        break

    print("Player 2 Position:", position2)
    
    #PLAYER 3:
    
    input("Player 3: Press Enter to roll the dice...")
    dice = random.randint(1, 6)
    print("Player 3 rolled:", dice)
    position3 += dice

    if position3 >= 50:
        print("Player 3 Wins!")
        break

    print("Player 3 Position:", position3)
    
    #PLAYER 4:
    
    input("Player 4: Press Enter to roll the dice...")
    dice = random.randint(1, 6)
    print("Player 4 rolled:", dice)
    position4 += dice

    if position4 >= 50:
        print("Player 4 Wins!")
        break
        
    print("Player 4 Position:", position4)
