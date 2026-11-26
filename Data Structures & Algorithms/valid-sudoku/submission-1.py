from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(len(board))]
        cols = [[] for _ in range(len(board))]
        squares = [[] for _ in range(len(board))]

        for i in range(len(board)):
            for j in range (len(board[i])):
                if board[i][j] == ".":
                    continue
                rows[i].append(int(board[i][j]))
                cols[j].append(int(board[i][j]))
                
                square_index = (i // 3) * 3 + (j // 3)
                squares[square_index].append(int(board[i][j]))

        for i in rows:
            if len(set(i)) != len(i):
                return False
        for j in cols:
            if len(set(j)) != len(j):
                return False
        for s in squares:
            if len(set(s)) != len(s):
                return False
        return True


