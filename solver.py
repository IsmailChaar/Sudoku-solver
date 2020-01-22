# Sudoku Solver with Backtracking
# 1) Trouvez un espace vide
# 2) Essayez de placer les chiffres 1-9 dans cet espace
# 3) Vérifiez si ce chiffre est valide à l'emplacement actuel en fonction de la matrice actuelle
#   a. Si le chiffre est valide, essayez récursivement de remplir le tableau en suivant les étapes 1 à 3.
#   b. S'il n'est pas valide, réinitialisez le carré que vous venez de remplir et revenez à l'étape précédente.
# 4) Une fois que la carte est pleine par la définition de cet algorithme, nous avons trouvé une solution.

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):  # bo : the board, num : the number we intend to check, pos : its position
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and i != pos[1]:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and i != pos[0]:
            return False

    # Check box
    box_x = pos[0] // 3
    box_y = pos[1] // 3

    for i in range(box_x * 3, box_x * 3 + 3):
        for j in range(box_y * 3, box_y * 3 + 3):
            if bo[i][j] == num and pos != (i, j):
                return False
    return True


# finds an empty space (zero)
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j  # (ligne, colonne)
    return None


# prints the board

def print_board(bo):
    for i in range(len(bo)):
        if i != 0 and i % 3 == 0:
            print("-------------------------")
        for j in range(len(bo[0])):
            if j != 0 and j % 3 == 0:
                print(" | ", end=" ")
            if j == 8:
                print(bo[i][j])
            else:
                print(bo[i][j], end=" ")


print_board(board)
print(" ")
print("Solving ...")
print(" ")
solve(board)
print_board(board)
