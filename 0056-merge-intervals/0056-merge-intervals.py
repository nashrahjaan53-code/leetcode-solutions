class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return[]

        intervals.sort(key=lambda x:x[0])
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            current_start, current_end = intervals[i]
            last_start, last_end = result[-1]

            if current_start <= last_end:
                result[-1][1] = max(last_end, current_end)
            else:
                result.append([current_start, current_end])

        return result
         



    