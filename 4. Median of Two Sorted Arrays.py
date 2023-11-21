class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        combined_l = len(nums1) + len(nums2)
        combined = sorted(nums1+nums2)
        
        if combined_l % 2 == 1:
            mid = (len(nums1) + len(nums2)) // 2
            return combined[mid]
        else:
            r = len(combined) // 2
            l = r - 1
            return (combined[l] + combined[r]) / 2

# Another solution
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        combined_l = len(nums1) + len(nums2)
        combined = sorted(nums1+nums2)
        
        if combined_l % 2 == 1:
            mid = (len(nums1) + len(nums2)) // 2
            return combined[mid]
        else:
            l = 0
            r = len(combined) - 1
            while l < r:
                l+=1
                r-=1
            return (combined[l-1]+ combined[r+1]) / 2