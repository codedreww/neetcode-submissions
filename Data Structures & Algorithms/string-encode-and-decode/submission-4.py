class Solution:

    def encode(self, strs: List[str]) -> str:
        retstr = ""
        for i in strs:
            x = str(len(i))
            retstr += "/"
            retstr += x
            retstr += "/"
            for j in i:
                retstr += j
        return retstr


    def decode(self, s: str) -> List[str]:
        i = 0
        x = 0
        num = ""
        retlist = []
        retstrs = ""
        while i < len(s) - 1:
            if s[i] == "/":
                i += 1
                while s[i] != "/":
                    num += s[i]
                    i += 1

                x = int(num)
                num = ""
                for j in range (i + 1, x + i + 1):
                    retstrs += s[j]
                retlist.append(retstrs)
                retstrs = ""
                i += (x + 1)

        return retlist
    
