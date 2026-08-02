class Solution:

    def encode(self, strs: List[str]) -> str:
        # put num and string together, so it would know how
        res = ""
        for n in strs:
            res += str(len(n))+"#"+n
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res

            
