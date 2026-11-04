class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += f'{len(word)}#{word}'
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        start = 0
        end = 0
        while end < len(s):
            if s[end] == '#':
                len_string = int(s[start:end])
                start = end + 1
                end = start + len_string
                decoded_string.append(s[start:end])
                start = end
                continue
            end += 1
        return decoded_string