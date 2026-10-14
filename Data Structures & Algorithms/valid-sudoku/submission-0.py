class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue  # skip empty cells
            
                # Row check
                if num in rows[i]:
                    return False
                rows[i].add(num)
            
                # Col check
                if num in cols[j]:
                    return False
                cols[j].add(num)
            
                # Box check
                box_index = (i // 3) * 3 + (j // 3)
                if num in boxes[box_index]:
                    return False
                boxes[box_index].add(num)
    
        return True