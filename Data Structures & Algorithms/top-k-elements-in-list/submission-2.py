from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictans = defaultdict(int)
        ret = []

        for i in nums:
            dictans[i] += 1

        for i in range (0, k):
            top_k = max(dictans, key=dictans.get)
            dictans.pop(top_k)
            ret.append(top_k)

        return ret
