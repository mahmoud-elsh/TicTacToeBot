table = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]


def printTable():
    for row in table:
        for value in row:
            print(value, end=" ")
        print(" ")
    print("----------------------------")

def userX():
    rowX = int(input("Type a row from 1 to 3."))
    if rowX < 1 or rowX > 3:
        print("Coordinates out of bounds, try again.")
        return False

    columnX = int(input("Type a column from 1 to 3."))
    if columnX < 1 or columnX > 3:
        print("Coordinates out of bounds, try again.")
        return False

    if table[rowX - 1][columnX - 1] == "X" or table[rowX - 1][columnX - 1] == "O":
        print("Coordinates already played, try again.")
        return False

    table[rowX - 1][columnX - 1] = "X"
    printTable()
    return True

def checkTie():
    if any("-" in nested_list for nested_list in table):
        pass
    else:
        return True

def userAi():
    bestScore = -100
    bestRow = 0
    bestValue = 0
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == "-":
                table[i][j] = "O"
                score = minimax(table, False)
                table[i][j] = "-"
                if score > bestScore:
                    bestScore = score
                    bestRow = i
                    bestValue = j
    table[bestRow][bestValue] = "O"
    printTable()

def minimax(table, isMaximizing):

    if check_winner(table) == "O":
        return 1
    if check_winner(table) == "X":
        return -1
    if not any("-" in nested_list for nested_list in table):
        return 0

    if isMaximizing:
        bestScore = -100
        for i in range(len(table)):
            for j in range(len(table[i])):
                if table[i][j] == "-":
                    table[i][j] = "O"
                    score = minimax(table, False)
                    table[i][j] = "-"
                    if score > bestScore:
                        bestScore = score
        return bestScore
    else:
        bestScore = 100
        for i in range(len(table)):
            for j in range(len(table[i])):
                if table[i][j] == "-":
                    table[i][j] = "X"
                    score = minimax(table, True)
                    table[i][j] = "-"
                    if score < bestScore:
                        bestScore = score
        return bestScore


def check_winner(table):
    if table[0][0] == table[1][1] == table[2][2] and table[0][0] != "-":
        return table[0][0]
    if table[0][2] == table[1][1] == table[2][0] and table[0][2] != "-":
        return table[0][2]
    if table[0][0] == table[0][1] == table[0][2] and table[0][0] != "-":
        return table[0][0]
    if table[1][0] == table[1][1] == table[1][2] and table[1][0] != "-":
        return table[1][0]
    if table[2][0] == table[2][1] == table[2][2] and table[2][0] != "-":
        return table[2][0]
    if table[0][0] == table[1][0] == table[2][0] and table[0][0] != "-":
        return table[0][0]
    if table[0][1] == table[1][1] == table[2][1] and table[0][1] != "-":
        return table[0][1]
    if table[0][2] == table[1][2] == table[2][2] and table[0][2] != "-":
        return table[0][2]
    return


game = True
while game:
    if checkTie():
        print("It's a tie!")
        break

    if not userX():
        continue
    else:
        userAi()

    if check_winner(table) == "O":
        print("User 2 has won!")
        break

    if check_winner(table) == "X":
        print("User 1 has won!")
        break

    if checkTie():
        print("It's a tie!")
        break
