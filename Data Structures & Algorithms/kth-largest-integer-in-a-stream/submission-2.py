class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # construct the minimum heap, but only push the largest value
        self.k = k
        if len(nums) <= k:
            self.min_heap_k = nums
            heapq.heapify(self.min_heap_k )
        else:
            self.min_heap_k = nums[:k]
            heapq.heapify(self.min_heap_k)
            for i in nums[k:]:
                self.add(i)
            
        

    def add(self, val: int) -> int:
        if len(self.min_heap_k) < self.k:
            heapq.heappush(self.min_heap_k, val)
        elif val > self.min_heap_k[0]:
            # first push, then pop the minimum
            # heapq.heappushpop(self.min_heap_k, val)
            heapq.heappop(self.min_heap_k)
            heapq.heappush(self.min_heap_k, val)

        
        return self.min_heap_k[0]
        
