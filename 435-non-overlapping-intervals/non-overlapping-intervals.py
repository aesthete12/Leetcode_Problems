class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])
        ans = 0
        currentEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < currentEnd:
                ans += 1
                currentEnd = min(currentEnd, end)
            else:
                currentEnd = end

        return ans