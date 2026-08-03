class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        l, r = 0, len(height)-1
        res = 0
        leftMax, rightMax = height[l], height[r]
        while l<r:
            if leftMax < rightMax:
                res += max(0, min(leftMax, rightMax) - height[l])
                l += 1
                leftMax = max(leftMax, height[l])
            else:
                res += max(0, min(leftMax, rightMax) - height[r])
                r -= 1
                rightMax = max(rightMax, height[r])
        return res

