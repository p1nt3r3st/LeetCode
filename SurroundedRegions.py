class Solution:
    def solve(self, board: list[list[str]]) -> None:

        def inBounds(i, j):
            return (0 <= i < n) and (0 <= j < m)
        """
        Do not return anything, modify board in-place instead.
        """

        o = "O"

        n = len(board)
        m = len(board[0])

        Q = []

        for i in range(n):
            if board[i][0] == o:
                Q.append((i, 0))
            if board[i][m - 1] == o:
                Q.append((i, m - 1))

        for j in range(m):
            if board[0][j] == o:
                Q.append((0, j))
            if board[n - 1][j] == o:
                Q.append((n - 1, j))

        while Q:
            i, j = Q.pop(0)
            board[i][j] = "#"

            for ii, jj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if not inBounds(ii, jj):
                    continue
                if board[ii][jj] != o:
                    continue
                Q.append((ii, jj))
                board[ii][jj] = '#'

        for i in range(n):
            for j in range(m):
                if board[i][j] == o:
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = o


solution = Solution()
board = [['X', 'X', 'X', 'X'],
         ['X', 'O', 'O', 'X'],
         ['X', 'X', 'O', 'X'],
         ['X', 'O', 'X', 'X']]

# board = [["O","O","O","O","X","X"],
#          ["O","O","O","O","O","O"],
#          ["O","X","O","X","O","O"],
#          ["O","X","O","O","X","O"],
#          ["O","X","O","X","O","O"],
#          ["O","X","O","O","O","O"]]
for c in board:
    print(*c)
print()
solution.solve(board)
for c in board:
    print(*c)

