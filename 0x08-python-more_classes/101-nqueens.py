def solveNQueens(n):
    def is_safe(board, row, col):
        # Check if there is a queen in the same column
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def backtrack(row):
        if row == n:
            # All queens are placed, add the current solution to the result
            result.append(board[:])
            return

        for col in range(n):
            if is_safe(board, row, col):
                # Place a queen at (row, col)
                board[row] = col
                # Move on to the next row
                backtrack(row + 1)
                # Backtrack: remove the queen from (row, col) for other possibilities
                board[row] = -1

    result = []
    # Initialize the board with no queens placed (-1 represents an empty cell)
    board = [-1] * n
    backtrack(0)
    
    # Format the result as a list of lists representing the placement of queens
    formatted_result = [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]
    return formatted_result
