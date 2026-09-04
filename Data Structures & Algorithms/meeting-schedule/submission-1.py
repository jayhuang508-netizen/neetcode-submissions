"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i: i.start)
        if len(intervals) == 0:
            return True
        last_interval = intervals[0]
        for i in intervals[1:]:
            if i.start < last_interval.end:
                return False
            last_interval = i
        return True

