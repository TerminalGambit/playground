from typing import List

class Solution:
    @staticmethod
    def gameOfLife(board: List[List[int]]) -> None:
        n = len(board)
        m = len(board[0])

        # Create a copy of the original board
        original = [[board[i][j] for j in range(m)] for i in range(n)]

        def count_neighbours(i, j) -> int:
            var = 0
            for x in range(max(0, i - 1), min(n, i + 2)):
                for y in range(max(0, j - 1), min(m, j + 2)):
                    if (x != i or y != j) and original[x][y] == 1:
                        var += 1
            return var

        for i in range(n):
            for j in range(m):
                count = count_neighbours(i, j)
                if original[i][j] == 1:
                    if count < 2 or count > 3:
                        board[i][j] = 0
                    elif 2 <= count <= 3:
                        board[i][j] = 1
                else:
                    if count == 3:
                        board[i][j] = 1
