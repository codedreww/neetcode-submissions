class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = None
        nums.sort()
        for i in nums:
            if i == x:
                return True
            x = i
        return False