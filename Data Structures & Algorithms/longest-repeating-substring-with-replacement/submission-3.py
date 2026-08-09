class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        r, l = 0,0
        n = len(s)
        longest = 0
        # because all upper case, use array as checking
        check_array = [0] * 26
        while r<n:
            idx = ord(s[r]) - ord('A')
            check_array[idx] += 1
            while sum(check_array) - max(check_array) > k:
                l_idx = ord(s[l]) - ord('A')
                check_array[l_idx] -= 1
                l += 1
            longest = max(longest, r-l+1)
            r += 1
        return longest



