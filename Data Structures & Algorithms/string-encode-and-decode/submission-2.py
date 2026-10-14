class Solution:

    def encode(self, strs: List[str]) -> str:
        retStr = ''
        for i in strs:
            retStr += str(len(i)) + '#' + i
        return retStr

    def decode(self, s: str) -> List[str]:
        retList = []

        i = 0
        while i < len(s):
        # read number until '#'
            num = ''
            while s[i].isdigit():
                num += s[i]
                i += 1
    
            # skip '#'
            i += 1
    
            # grab the string
            length = int(num)
            retList.append(s[i : i + length])
    
            # move pointer to end of string
            i+= length

        return retList










            

            

