class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negNums = [-n for n in nums]
        heapq.heapify(negNums)
        
        for _ in range(k-1):
            heapq.heappop(negNums)
        return -negNums[0]



        