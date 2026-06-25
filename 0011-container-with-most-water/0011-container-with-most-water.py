class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            width = right - left
            min_height = min(height[left],height[right])
            area = width * min_height
            max_water = max(max_water, area)

            if height[left] < height[right]:
                current_left = height[left]
                while left < right and height[left] <= current_left:
                    left +=1
            else:
                current_right = height[right]
                while left < right and height[right] <= current_right:
                    right -= 1
        return max_water
    



        