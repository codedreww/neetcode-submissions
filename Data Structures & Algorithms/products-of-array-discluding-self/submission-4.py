class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        ret = [1] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                left[i] = nums[i]
            else:
                left[i] = nums[i] * left[i - 1]

        for j in range(len(nums) - 1, -1, -1):
            if j == len(nums) - 1:
                right[j] = nums[j]
            else:
                right[j] = nums[j] * right[j + 1]

        for i in range(len(nums)):
            if i != 0 and i != len(nums) - 1:
                ret[i] = left[i - 1] * right[i + 1]
            elif i == 0:
                ret[i] = right[i + 1]
            else:
                ret[i] = left[i - 1]
        return ret



                