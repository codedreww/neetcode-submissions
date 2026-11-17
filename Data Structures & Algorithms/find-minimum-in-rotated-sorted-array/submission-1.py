class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                # drop is to the right of mid, so mid can't be the min
                l = mid + 1
            else:
                # mid..r is sorted, so the min is mid or to its left
                r = mid

        return nums[l]