class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            minheight = min(heights[left], heights[right])
            curr = minheight * (right - left)
            if curr > area :
                area = curr

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return area