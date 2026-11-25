class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seen = set(nums)
        res = 1

        for i in range(len(nums)):
            length = 0
            if (nums[i] - 1) in seen:
                continue
            else:
                x = nums[i]
                while x in seen:
                    length += 1
                    x += 1
                res = max(res, length)

        return res
