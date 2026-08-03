class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) -1
        # each move should have gains
        area = min(heights[i],heights[j])*(j-i)
        #smaller one move towards the higher one and check the size
        while i<j:
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
            temp_area = min(heights[i],heights[j])*(j-i)
            area = max(area, temp_area)
        return area
            

        