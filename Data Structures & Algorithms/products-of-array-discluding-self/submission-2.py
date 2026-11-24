class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [1] * len(nums)
        zeros = 0
        total_sum = 1

        for i in nums:
            if i == 0:
                zeros += 1
            else:
                total_sum *= i


        if zeros >= 2:
            return [0] * len(nums)

        elif zeros == 1:
            for i in range (0,len(nums)):
                if nums[i] != 0:
                    ret[i] = 0
                else:
                    ret[i] = total_sum
        else:
            for i in range (0,len(nums)):
                ret[i] = total_sum // nums[i]

        return ret

                