#You are given a binary array nums, return the maximum number of consecutive 1's in the array.
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        max_count = 0

        for i in range(n):
            count = 0
            for j in range(i, n):
                if nums[j] == 0:
                    break
                count += 1
                max_count = max(max_count, count)
        return max_count




