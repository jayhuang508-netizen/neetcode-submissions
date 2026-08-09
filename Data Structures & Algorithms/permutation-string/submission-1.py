class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)< len(s1):
            return False
        window_size = len(s1)
        # they only contain lowercase letters
        # so it could use letter array, then use tuple to check them
        s1_array = [0]*26
        for s in s1:
            s1_array[ord(s)-ord('a')] += 1
        s1_tuple = tuple(s1_array)

        # use sliding window for s2 to check whether it contains the same tuple
        s2_array = [0]*26
        # first put the window size elements to check
        r = 0
        l = 0
        for i in range(window_size):
            s2_array[ord(s2[r])-ord('a')] += 1
            r+= 1
        s2_tuple = tuple(s2_array)
        if s2_tuple == s1_tuple:
            return True
        while r < len(s2):
            s2_array[ord(s2[r])-ord('a')] += 1
            s2_array[ord(s2[l])-ord('a')] -= 1
            s2_tuple = tuple(s2_array)
            if s2_tuple == s1_tuple:
                return True
            r += 1
            l +=1
        return False


            


