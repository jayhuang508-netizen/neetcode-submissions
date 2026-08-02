from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = defaultdict(int)
        for n in nums:
            count_dict[n] +=1
        
        sorted_count_dict = dict(sorted(count_dict.items(), key = lambda item: item[1], reverse = True))
        return list(sorted_count_dict.keys())[:k]