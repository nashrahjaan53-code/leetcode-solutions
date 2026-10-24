class Solution:
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def to_day(date):
            m,d = map(int, date.split('-'))
            return sum(days[:m-1]) + d
        a1 = to_day(arriveAlice)
        a2 = to_day(leaveAlice)
        b1 = to_day(arriveBob)
        b2 = to_day(leaveBob)
        start = max(a1, b1)
        end = min(a2, b2)
        return max(0, end - start + 1) 