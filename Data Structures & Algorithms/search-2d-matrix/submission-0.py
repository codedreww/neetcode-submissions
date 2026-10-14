class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lrow, rrow = 0, len(matrix) - 1

        while lrow <= rrow:
            mid = (lrow + rrow) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                # Step 2: binary search inside the row
                row = matrix[mid]
                lcol, rcol = 0, len(row) - 1
                while lcol <= rcol:
                    mcol = (lcol + rcol) // 2
                    if row[mcol] == target:
                        return True
                    elif row[mcol] < target:
                        lcol = mcol + 1
                    else:
                        rcol = mcol - 1
                return False
            elif target < matrix[mid][0]:
                rrow = mid - 1
            else:
                lrow = mid + 1

        return False

        