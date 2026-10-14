class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = -1  # last valid element

        for r in range(len(nums)):
            if nums[r] != val:
                l += 1
                nums[l], nums[r] = nums[r], nums[l]

        return l + 1
