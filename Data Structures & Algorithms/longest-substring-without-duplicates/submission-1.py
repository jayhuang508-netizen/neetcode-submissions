class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arrary_check = [0]*256
        r = l = 0
        n = len(s)
        length = 0
        while r < n:
            idx = ord(s[r])
            while arrary_check[idx]!= 0:
                left_idx = ord(s[l])
                arrary_check[left_idx] -= 1
                l += 1
            arrary_check[idx] += 1
            length = max(length, (r-l+1))
            r += 1
        return length
        