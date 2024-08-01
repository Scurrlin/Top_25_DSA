class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totalArray = nums1 + nums2
        totalArray.sort()
        size = len(totalArray)
        if(size % 2 == 0):
            size1 = size // 2
            size2 = (size // 2) - 1
            return (float((totalArray[size1] + totalArray[size2]) / 2 ))
        else:
            size1 = size // 2
            return float(totalArray[size1])