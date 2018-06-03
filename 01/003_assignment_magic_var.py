def pick_num():
    magic_num = 6
    while True:

        user_pick = int(input("Enter a number between 0 and 10: "))
        if magic_num == user_pick:
            print("You've won! Congrats!")
            break
        else:
            print("Wrong number! Try again!")
            continue
pick_num()
