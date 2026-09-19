class Solution:
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))
        dx = closest_x - xCenter
        dy = closest_y - yCenter
        dist_sq = dx * dx + dy * dy
        return dist_sq <= radius * radius





        