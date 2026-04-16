
class Soltion:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_numbers = set()
        for num in nums:
            if num in seen_numbers:
                return True
            seen_numbers.add(num)

        return False

"""
Both solutions have a space complexity od O(n)
The second has a time complexity of O(n)

Not sure about the first
"""