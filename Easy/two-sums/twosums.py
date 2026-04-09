# Compleixty O(n^2)
## My solution utilises a brute force approach . I am very much a begineer getting better at DSA
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        output = []
        for i in range(n):
            for j in range(n):
                while i < j:
                    if nums[i] + nums[j] == target:
                        output.extend([i,j])
                    break
        return output


# For complexity O(n)
class solution:
    def twosum(self, nums: List[int], target: int) -> List[int]:
        l = 0 #left index
        r = len(nums) - 1 #right index
        while(l < r):
            result = nums[l] + nums[r]
            if result == target:
                return [l, r]
            elif result < target:
                l += 1
            else:
                r -= 1
        return []

