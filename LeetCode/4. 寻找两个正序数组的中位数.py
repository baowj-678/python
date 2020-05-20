# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。

# 请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

# 你可以假设 nums1 和 nums2 不会同时为空。

# 示例 1:

# nums1 = [1, 3]
# nums2 = [2]

# 则中位数是 2.0
# 示例 2:

# nums1 = [1, 2]
# nums2 = [3, 4]

# 则中位数是 (2 + 3)/2 = 2.5


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)
        if(n > m):
            n, m, nums1, nums2 = m, n, nums2, nums1
        imin = 0
        imax = n - 1
        if(imin == imax):
            jRight = m // 2
            if(m % 2 == 0):
                jLeft = jRight - 1
                if(nums2[jLeft] > nums1[imin]):
                    return nums2[jLeft]
                elif(nums2[jRight] < nums1[imin]):
                    return nums2[jRight]
                else:
                    return nums1[imin]
            else:
                if(n == 1):
                    return (n + m) / 2.0
                else:
                    j = jRight
                    jRight = jRight + 1
                    jLeft = j - 1
                    if(nums1[imin] < nums2[jLeft]):
                        return (nums2[jLeft] + nums2[j]) / 2
                    elif(nums1[imin] > nums2[jRight]):
                        return (nums2[jRight] + nums2[j]) / 2
                    else:
                        return (nums1[imin] + nums2[j]) / 2

        while(imin < imax):
            print(imin, imax)
            iRight = (imin + imax) // 2 + 1
            jRight = (m + n) // 2 - iRight
            iLeft = iRight - 1
            jLeft = jRight - 1
            print(iLeft, iRight, jLeft, jRight)
            if(nums1[iLeft] > nums2[jRight]):
                imax = iRight
            elif(nums2[jLeft] > nums1[iRight]):
                imin = iRight
            else:
                if((m + n) % 2 == 0):
                    return max(nums1[iLeft], nums2[jLeft]) +\
                           min(nums1[iRight], nums2[jRight]) / 2.0
                else:
                    return min(nums1[iRight], nums2[jRight])
        return None


if(__name__ == "__main__"):
    s = Solution()
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(s.findMedianSortedArrays(nums1, nums2))


# pointOneLeft = 0
# pointOneRight = len(nums1)
# lenOne = pointOneRight
# pointTwoLeft = 0
# pointTwoRight = len(nums2)
# lenTwo = pointTwoRight
# while(lenOne > 2 and lenTwo > 2):
#     half = min(lenOne, lenTwo) // 2
#     numOneLeft = nums1[pointOneLeft + half]
#     numOneRight = nums1[pointOneRight - half]
#     numTwoLeft = nums2[pointTwoLeft + half]
#     numTwoRight = nums2[pointTwoRight - half]
#     if(numOneLeft < numTwoLeft):
#         pointOneLeft += half
#     else:
#         pointTwoLeft += half
#     if(numOneRight > numTwoRight):
#         pointOneRight -= half
#     else:
#         pointTwoRight -= half
#     lenOne = pointOneRight - pointOneLeft
#     lenTwo = pointTwoRight - pointTwoLeft
# if(lenOne == 1):
#     half = lenTwo // 2
#     if(half*2 == lenTwo):
#         numTwoLeft = nums2[pointTwoLeft + half - 1]
#         numTwoRight = nums2[pointTwoLeft + half]
#         numOneLeft = nums1[pointOneLeft]
#         if(numOneLeft < numTwoLeft):
#             return numTwoRight
#         elif(numOneLeft > numTwoRight):
#             return numTwoLeft
#         else:
#             return numOneLeft
#     else:
