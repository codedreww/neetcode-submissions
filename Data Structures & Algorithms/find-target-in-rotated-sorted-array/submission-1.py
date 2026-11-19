class Solution:
    def find_cut(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return l

    def search(self, nums: List[int], target: int) -> int:
        cut = self.find_cut(nums)
        l = 0
        r = len(nums) - 1

        if cut > 0 and nums[0] <= target <= nums[cut - 1]:
            r = cut - 1
        else:
            l = cut

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
                
        return -1