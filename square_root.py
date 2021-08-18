"""

LeetCode 
69. Sqrt(x)
"""


class Solution:
    def mySqrt(self, x: int) -> int:

        start = 0
        end = x  # 8

        while start <= end:

            mid = (start + end) // 2
            if mid * mid > x:
                if (mid - 1) * (mid - 1) < x:
                    return mid - 1
                end = mid - 1
            elif mid * mid < x:
                if (mid + 1) * (mid + 1) > x:
                    return mid
                start = mid + 1
            else:
                return mid
