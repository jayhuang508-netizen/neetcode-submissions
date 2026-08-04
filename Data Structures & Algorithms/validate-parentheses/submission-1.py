class Solution:
    def isValid(self, s: str) -> bool:
        rel_dict = {')': '(', '}':'{', ']': '['}
        left = set(rel_dict.keys())
        right = set(rel_dict.values())
        check_list = []
        for char in s:
            if char in right:
                check_list.append(char)
            else:
                if len(check_list)>0 and check_list[-1] == rel_dict[char]:
                    check_list.pop()
                else:
                    return False
        if len(check_list) > 0:
            return False
        return True