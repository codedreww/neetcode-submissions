class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        ret = []
        for i in nums:
            dic[i] += 1

        while k > 0:
            maxkey = max(dic, key=dic.get)
            maxval = dic[maxkey]
            ret.append(maxkey)
            del dic[maxkey]
            k -= 1

        return ret


        


