class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []

        for i in range (len(sorted_nums)):
            k = i + 1
            j = len(nums) - 1
            if sorted_nums[i] > 0:
                break
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue    
            while k < j:
                total = sorted_nums[i] + sorted_nums[k] + sorted_nums[j]
                if total == 0:
                    res.append([sorted_nums[i], sorted_nums[k], sorted_nums[j]])
                    k += 1
                    j -= 1
                    while k < j and sorted_nums[k] == sorted_nums[k - 1]:
                        k += 1    
                elif total < 0:
                    k += 1
                elif total > 0:
                    j -= 1
        return res



