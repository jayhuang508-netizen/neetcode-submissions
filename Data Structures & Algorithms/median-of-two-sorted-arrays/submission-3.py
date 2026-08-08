class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # recursively get rid of 
        def getkthsmallest(a, b, k):
            print(a, b, k)
            if len(a) > len(b):
                return getkthsmallest(b, a, k)
            if len(a) == 0:
                return b[k-1]
            if k == 1:
                return min(a[0], b[0])
            
            i = min(len(a), k//2)
            j = min(len(b), k//2)
            if a[ i - 1] > b[ j - 1]:
                return getkthsmallest(a,b[j:],k-j)
            else:
                return getkthsmallest(a[i:],b,k-i)
            
        left = (len(nums1) + len(nums2) + 1) // 2
        right = (len(nums1) + len(nums2) + 2) // 2
        return (getkthsmallest(nums1.copy(), nums2.copy(), left) +
                getkthsmallest(nums1.copy(), nums2.copy(), right)) / 2.0





        