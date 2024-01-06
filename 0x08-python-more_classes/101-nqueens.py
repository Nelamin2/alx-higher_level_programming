#!/usr/bin/python3
import sys

class NQueensSolver:
    """
    A class to solve the N-Queens problem.

    Attributes:
        n (int): Size of the chessboard.
        result (list): List to store solutions.
        board (list): Current placement of queens on the chessboard.
    """

    def __init__(self, n):
        """
        Initialize the NQueensSolver.

        Args:
            n (int): Size of the chessboard.
        """
        self.n = n
        self.result = []
        self.board = [-1] * n

    def is_safe(self, row, col):
        """
        Check if it's safe to place a queen at a given position.

        Args:
            row (int): Current row to consider.
            col (int): Column to check for placing a queen.

        Returns:
            bool: True if safe, False otherwise.
        """
        for i in range(row):
            if self.board[i] == col or \
               self.board[i] - i == col - row or \
               self.board[i] + i == col + row:
                return False
        return True

    def backtrack(self, row):
        """
        Backtracking algorithm to find solutions for N-Queens.

        Args:
            row (int): Current row being considered.
        """
        if row == self.n:
            self.result.append(self.board[:])
            return
        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row] = col
                self.backtrack(row + 1)
                self.board[row] = -1

    def solve_nqueens(self):
        """
        Solve the N-Queens problem and print solutions.

        Prints:
            Every possible solution to the N-Queens problem, one solution per line.
            Format: List of queen positions [row, col].
        """
        self.result = []
        self.backtrack(0)

        for solution in self.result:
            print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)

        # Example usage
        solver = NQueensSolver(n)
        solver.solve_nqueens()
    except ValueError:
        print("N must be a number")
        sys.exit(1)

