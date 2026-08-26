class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # always take the heaviest two
        # maximum heap, pop twice and put back, until last one left
        reversed_stone = [-s for s in stones]
        heapq.heapify(reversed_stone)
        while len(reversed_stone) > 1:
            stone1 = heapq.heappop(reversed_stone)
            stone2 = heapq.heappop(reversed_stone)
            crush = -abs(stone1 - stone2)
            heapq.heappush(reversed_stone, crush)
        if len(reversed_stone) == 1:
            return -reversed_stone[0]
        else:
            return 0