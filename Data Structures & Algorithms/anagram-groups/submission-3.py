
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_result = {}
        def constructTuple(string):
            # contruct count dict for single str
            # dict is not hashable, construct it into a string with char+num
            count_str = {}
            for s in string:
                count_str[s] = 1 + count_str.get(s,0)
            count_str = dict(sorted(count_str.items()))
            return tuple(count_str.items())
        for string in strs:
            hash_s = hash(constructTuple(string))
            if hash_s in group_result:
                group_result[hash_s].append(string)
            else:
                group_result[hash_s] = [string]
        return [v for k,v in group_result.items()]

        