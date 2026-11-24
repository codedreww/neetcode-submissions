class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [1] * n

        # pass 1: ret[i] = product of everything before i
        for i in range(1, n):
            ret[i] = ret[i - 1] * nums[i - 1]

        # pass 2: multiply in the product of everything after i
        right = 1
        for i in range(n - 1, -1, -1):
            ret[i] *= right
            right *= nums[i]

        return ret