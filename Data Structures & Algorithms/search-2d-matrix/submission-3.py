class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_l = 0
        row_r = len(matrix) - 1

        while row_l <= row_r:
            row_mid = (row_r + row_l) // 2
            lower_bound = matrix[row_mid][0]
            upper_bound = matrix[row_mid][len(matrix[row_mid]) - 1]

            if lower_bound <= target <= upper_bound:
                l = 0
                r = len(matrix[row_mid]) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if target == matrix[row_mid][mid]:
                        return True
                    elif target < matrix[row_mid][mid]:
                        r = mid - 1
                    elif target > matrix[row_mid][mid]:
                        l = mid + 1
                return False
            elif target < lower_bound:
                row_r = row_mid - 1
            elif target > upper_bound:
                row_l = row_mid + 1

        return False