class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        targetDict = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in targetDict:
                return[targetDict[complement] + 1, i + 1]
            targetDict[num] = i
        return None