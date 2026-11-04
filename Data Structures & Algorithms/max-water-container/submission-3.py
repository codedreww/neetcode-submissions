class Solution:
    def maxArea(self, heights: List[int]) -> int:
        x1 = 0
        x2 = len(heights) - 1
        max_area = 0

        while x1 < x2:
            curr_area = (min(heights[x1], heights[x2])) * ((x2 + 1) - (x1 + 1))
            if curr_area > max_area:
                max_area = curr_area
            if heights[x1] >= heights[x2]:
                x2 -= 1
            else:
                x1 += 1
        return max_area

