class Solution:
    def findMin(self, nums: List[int]) -> int:
        # the cut position is the min num
        l, r = 0, len(nums)-1
        res = nums[0]
        while l<=r:
            if nums[l] < nums[r]:
                # the farest still maintain the order
                res = min(res, nums[l])
                break
            mid = l + ( r - l )//2
            res = min(res, nums[mid])
            if nums[l] <= nums[mid]:
                l = mid+1
            else:
                r = mid -1
        return res

            

        