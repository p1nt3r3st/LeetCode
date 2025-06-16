class Solution(object):
    def snakesAndLadders(self, board):
        n = len(board)
        min_rolls = [-1] * (n * n + 1)
        q = []
        min_rolls[1] = 0
        q.append(1)

        while q:
            x = q.pop(0)
            for i in range(1, 7):
                t = x + i
                if t > n * n:
                    break
                row = (t - 1) // n
                col = (t - 1) % n
                v = board[n - 1 - row][(n - 1 - col) if (row % 2 == 1) else col]
                y = v if v > 0 else t
                if y == n * n:
                    return min_rolls[x] + 1
                if min_rolls[y] == -1:
                    min_rolls[y] = min_rolls[x] + 1
                    q.append(y)
        return -1


solution = Solution()

board = [[-1,-1,30,14,15,-1],
         [23,9,-1,-1,-1,9],
         [12,5,7,24,-1,30],
         [10,-1,-1,-1,25,17],
         [32,-1,28,-1,-1,32],
         [-1,-1,23,-1,13,19]]

print(solution.snakesAndLadders(board))

