class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        ret = 1
        temp = 1

        if len(nums) == 1:
            return ret
        if not nums:
            return 0

        for i in range (1, len(nums_sorted)):
            if nums_sorted[i - 1] + 1 == nums_sorted[i]:
                temp += 1
                ret = max(ret, temp)
            elif nums_sorted[i - 1] == nums_sorted[i]:
                continue
            else:
                temp = 1
        return ret
