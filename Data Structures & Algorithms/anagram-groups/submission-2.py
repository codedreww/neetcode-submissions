class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # Mappting charCount to list of anagrams

        for s in strs:
            count = [0] * 26  # a to z

            for c in s:
                count[ord(c) - ord("a")] += 1  # ord is checking the ascii value, so if we're checking a, a - a = 0

            res[tuple(count)].append(s)  # We have to convert count to tuple since python wouldnt allow a list to be keys
        return list(res.values())