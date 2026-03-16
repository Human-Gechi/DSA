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

## My solution utilises a brute force approach . I am very much a begineer getting better at DSA

# Poco A poco