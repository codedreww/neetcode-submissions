class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        counter = 1

        while counter < len(nums):
            ans[counter] = nums[counter - 1] * ans[counter - 1]
            counter += 1

        counter -= 1
        suf = 1
        while counter >= 0:
            ans[counter] *= suf
            suf *= nums[counter]
            counter -= 1

        return ans