class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        target = (m+n)/2
        if target == 0:
            if m > 0:
                return nums1[0] * 2 / 2.0
            elif n > 0:
                return nums2[0] * 2 / 2.0
            else:
                return 0.0
        if (m+n) % 2 != 0:
            ret = self.findKthNum(nums1, nums2, target) * 2 / 2.0
        else:
            ret = ( self.findKthNum(nums1, nums2, target-1) + self.findKthNum(nums1, nums2, target) ) / 2.0
        return ret


    def findKthNum(self, nums1, nums2, k):
        m = len(nums1)
        n = len(nums2)
        if m == 0:
            if k < n:
                return nums2[k]
            else:
                return None
        if n == 0:
            if k < m:
                return nums1[k]
            else:
                return None
        i = 0
        j = 0
        nowIdx = 0
        while (i<m and j <n):
            #print nowIdx, i, j, k
            if nums1[i] <= nums2[j]:
                if nowIdx == k:
                    return nums1[i]
                else:
                    nowIdx += 1
                    i += 1
            else:
                if nowIdx == k:
                    return nums2[j]
                else:
                    j += 1
                    nowIdx += 1
        if i == m:
            return nums2[k-nowIdx+j]
        if j == n:
            return nums1[k-nowIdx+i]


if __name__ == '__main__':
    s = Solution()
    nums1 = [2,3]
    nums2 = [1]
    print s.findMedianSortedArrays(nums1, nums2)
    #for i in range(len(nums1)+len(nums2)):
    #    print s.findKthNum(nums1, nums2, i)
