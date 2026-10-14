class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict

        my_dict = defaultdict(int)

        for i in s:
            my_dict[i] += 1

        for j in t:
            if j in my_dict:
                if my_dict[j] > 1:
                    my_dict[j] -= 1
                else:
                    del my_dict[j]
            else:
                return False

        if len(my_dict) != 0:
            return False

        return True