class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        res = []

        for i, value in enumerate(nums):
            req_val = target - value
            if req_val in seen:
                res.append(seen[req_val])
                res.append(i)
                return res
            
            seen[value] = i
        
        return None