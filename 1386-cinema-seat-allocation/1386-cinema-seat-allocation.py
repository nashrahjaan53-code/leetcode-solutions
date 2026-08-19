class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        reserved = {}
        for row, seat in reservedSeats:
            if row not in reserved:
                reserved[row] = set()
            reserved[row].add(seat)
        ans = 0
        for seats in reserved.values():
            left = not(seats & {2,3,4,5})
            mid = not(seats & {4,5,6,7})
            right = not(seats &{6,7,8,9})
            if left and right:
                ans += 2
            elif left or mid or right:
                ans += 1
        empty_rows = n - len(reserved)
        ans += empty_rows * 2

        return ans





        