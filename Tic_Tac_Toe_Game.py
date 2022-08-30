def Print_Board(xstate, zstate):
    one = "X" if(xstate[0]==1) else("O" if zstate[0]==1 else 1)
    two = "X" if(xstate[1]==1) else("O" if zstate[1]==1 else 2)
    three = "X" if(xstate[2]==1) else("O" if zstate[2]==1 else 3)
    four = "X" if(xstate[3]==1) else("O" if zstate[3]==1 else 4)
    five = "X" if(xstate[4]==1) else("O" if zstate[4]==1 else 5)
    six = "X" if(xstate[5]==1) else("O" if zstate[5]==1 else 6)
    seven = "X" if(xstate[6]==1) else("O" if zstate[6]==1 else 7)
    eight = "X" if(xstate[7]==1) else("O" if zstate[7]==1 else 8)
    nine = "X" if(xstate[8]==1) else("O" if zstate[8]==1 else 9)
    print(f"{one} | {two} | {three}")
    print("--|---|--")
    print(f"{four} | {five} | {six}")
    print("--|---|--")
    print(f"{seven} | {eight} | {nine}")


def Check_Win(xstate, zstate):
    win = [[0,1,2], [3,4,5], [6,7,8], [0,4,8], [2,4,6], [0,3,6], [1,4,7], [2,4,8]]
    for case in win:
        if(xstate[case[0]]+xstate[case[1]]+xstate[case[2]]==3):
            Print_Board(xstate,zstate)
            print("X Won The Game.")
            return 1
        elif(zstate[case[0]]+zstate[case[1]]+zstate[case[2]]==3):
            Print_Board(xstate,zstate)
            print("O Won The Game.")
            return 0
    return -1


xstate = [0,0,0,0,0,0,0,0,0]
zstate = [0,0,0,0,0,0,0,0,0]
turn = 1
chances = 0
while(chances<9):
    Print_Board(xstate,zstate)
    if turn==1:
        print("X's Turn: ")
        position = int(input("Enter the position where you want to make a move: "))
        xstate[position-1] = 1
    else:
        print("O's Turn: ")
        position = int(input("Enter the position where you want to make a move: "))
        zstate[position-1] = 1
    cwin = Check_Win(xstate,zstate)
    if(cwin!=-1):
        print("Game Over!!")
        break
    chances = chances + 1
    turn = 1 - turn
