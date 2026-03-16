#You are given a binary array nums, return the maximum number of consecutive 1's in the array.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        data = 1
        count = 0
        max_count = 0
        for val in nums:
            if val == data:
                count += 1
                if count >= max_count:
                    max_count = count
            else:
                    count = 0
        return max_count




