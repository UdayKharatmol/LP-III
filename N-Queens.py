def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] or (col - row + i >= 0 and board[i][col - row + i]) or (col + row - i < n and board[i][col + row - i]):
            return False
    return True

def place_queens(board, row, n):
    if row == n: return True
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if place_queens(board, row + 1, n): return True
            board[row][col] = 0
    return False

def print_board(board, n):
    for row in board:
        print(" ".join(str(x) for x in row))

n = int(input("Enter the number of queens: "))
board = [[0] * n for _ in range(n)]

if place_queens(board, 0, n):
    print("N-Queens Matrix:")
    print_board(board, n)
else:
    print("No solution exists")
