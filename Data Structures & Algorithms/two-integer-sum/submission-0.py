from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        my_dict = defaultdict(int)
        for i in range (0, len(nums)):
            difference = target - nums[i]
            if difference in my_dict:
                output.append(my_dict[difference])
                output.append(i)
                return output
            my_dict[nums[i]] += i