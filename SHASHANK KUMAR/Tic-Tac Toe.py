def enter(p):
    if pos == 1:
        if p == "Player1":
            tab[0][0] = "X"
        else:
            tab[0][0] = "O"
    elif pos == 2:
        if p == "Player1":
            tab[0][1] = "X"
        else:
            tab[0][1] = "O"
    elif pos == 3:
        if p == "Player1":
            tab[0][2] = "X"
        else:
            tab[0][2] = "O"
    elif pos == 4:
        if p == "Player1":
            tab[1][0] = "X"
        else:
            tab[1][0] = "O"
    elif pos == 5:
        if p == "Player1":
            tab[1][1] = "X"
        else:
            tab[1][1] = "O"
    elif pos == 6:
        if p == "Player1":
            tab[1][2] = "X"
        else:
            tab[1][2] = "O"
    if pos == 7:
        if p == "Player1":
            tab[2][0] = "X"
        else:
            tab[2][0] = "O"
    elif pos == 8:
        if p == "Player1":
            tab[2][1] = "X"
        else:
            tab[2][1] = "O"
    elif pos == 9:
        if p == "Player1":
            tab[2][2] = "X"
        else:
            tab[2][2] = "O"
    for i in tab:
        print(*i, sep="\t")


def check_for_win():
    if tab[0][0] == tab[0][1] == tab[0][2] or tab[1][0] == tab[1][1] == tab[1][2] or tab[2][0] == tab[2][1] == tab[2][2]:
        return True
    elif tab[0][0] == tab[1][0] == tab[2][0] or tab[0][1] == tab[1][1] == tab[2][1] or tab[0][2] == tab[1][2] == tab[2][2]:
        return True
    elif tab[0][0] == tab[1][1] == tab[2][2] or tab[0][2] == tab[1][1] == tab[2][0]:
        return True

def check_for_draw(count):
    if count>=9 and not check_for_win():
        return True

tab = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in tab:
    print(*i,sep = "\t")
count = 0
positions = []
while True:
    p = "Player1"
    print("Player1's turn: ")
    while True:
        try:
            pos = int(input("Enter position: "))
        except ValueError:
            print("Enter valid position!")
            continue
        if pos in positions:
            print("Postion already occupied!")
            continue
        elif pos<1 or pos>9:
            print("Position out of range!")
            continue
        else:
            positions.append(pos)
            enter(p)
            break
    count+=1
    if check_for_win():
        print("Player1 is the winner!")
        break
    if check_for_draw(count):
        print("Its a draw!")
        break
    p = "Player2"
    print("Player2's turn: ")
    while True:
        try:
            pos = int(input("Enter position: "))
        except ValueError:
            print("Enter valid position!")
            continue
        if pos in positions:
            print("Postion already occupied!")
            continue
        elif pos<1 or pos>9:
            print("Position out of range!")
            continue
        else:
            positions.append(pos)
            enter(p)
            break
    count+=1
    if check_for_win():
        print("Player2 is the winner!")
        break
    if check_for_draw(count):
        print("Its a draw!")
        break
