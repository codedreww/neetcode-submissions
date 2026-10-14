class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 2:
            return 2
        if n == 1:
            return 1

        b = [0] * n
        b[0] = 1
        b[1] = 2

        for k in range (2, n):
            b[k] = b[k - 1] + b[k - 2]

        return b[n - 1]

