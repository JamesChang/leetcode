class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        expected1 = (len_nums1 + len_nums2 -1)/2
        expected2 = (len_nums1 + len_nums2 )/2
        result1 = 0
        result2 = 0
        i=0
        
        for x in self.mergeSort(nums1, nums2):
           if i == expected1:
               result1 = x
           if i == expected2:
               result2 = x
               return float(result1 + result2)/2
            
           i +=1
        
    def mergeSort(self, nums1, nums2):
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        i = 0
        j = 0
        while(i<len_nums1 or j<len_nums2):
            x = nums1[i] if i < len_nums1 else None
            y = nums2[j] if j < len_nums2 else None
            if x is None and y is None:
                break
            if x is not None and (x <= y or y is None):
                yield nums1[i]
                i += 1
            else:
                yield nums2[j]
                j += 1