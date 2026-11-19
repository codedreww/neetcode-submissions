from collections import defaultdict
class TimeMap:


    def __init__(self):
        self.storage = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ts = self.storage.get(key)

        if ts == None or ts == []:
            return ""
        
        l = 0
        r = len(ts) - 1
        res = ""

        if timestamp >= ts[r][1]:
            return ts[r][0]
        elif timestamp < ts[l][1]:
            return ""

        while l <= r:
            mid = (l + r) // 2
            if ts[mid][1] <= timestamp:
                res = ts[mid][0]
                l = mid + 1
            elif ts[mid][1] > timestamp:
                r = mid - 1
            
        return res