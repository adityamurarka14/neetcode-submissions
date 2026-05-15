class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        smaller, larger = nums1, nums2
        if len(larger) < len(smaller):
            smaller, larger = larger, smaller
        
        totalLen = len(nums1) + len(nums2)
        midEle = totalLen // 2
        
        left, right = 0, len(smaller) - 1
        while True:
            mid = (left + right) // 2
            rem = midEle - mid - 2

            smallerLeft = smaller[mid] if mid >= 0 else float("-infinity")
            smallerRight = smaller[mid + 1] if (mid + 1) < len(smaller) else float("infinity")
            biggerLeft = larger[rem] if rem >= 0 else float("-infinity")
            biggerRight =  larger[rem + 1] if (rem + 1) < len(larger) else float("infinity")

            if smallerLeft <= biggerRight and biggerLeft <= smallerRight:
                if totalLen % 2:
                    return min(smallerRight, biggerRight)
                else:
                    return (max(smallerLeft, biggerLeft) + min(smallerRight, biggerRight)) / 2
            elif smallerLeft > biggerRight:
                right = mid - 1
            else:
                left = mid + 1