class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = dict()
        t_dict = dict()
        for c in s:
            if c in s_dict:
                s_dict[c] += 1
            else:
                s_dict[c] = 0
        for c in t:
            if c in t_dict:
                t_dict[c] += 1
            else:
                t_dict[c] = 0
        for k,v in s_dict.items():
            if k not in t_dict:
                return False
            if t_dict[k] != v:
                return False

        return True
        