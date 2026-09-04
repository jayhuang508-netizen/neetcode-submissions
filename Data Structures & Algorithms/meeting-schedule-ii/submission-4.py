"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # record several last end
        intervals.sort(key=lambda i: i.start)
        if len(intervals) == 0:
            return 0
        ends = [intervals[0].end]
        heapq.heapify(ends)

        for i in intervals[1:]:
            # print(i.start, min(ends))
            if i.start < ends[0]:
                heapq.heappush(ends, i.end)
            else:
                heapq.heappop(ends)
                heapq.heappush(ends, i.end)
                # ends[0] = i.end
                
        # print(ends)
        return len(ends)
                


        