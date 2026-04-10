## Given an array of positive integers and a target sum,
# find the length of the smallest contiguous subarray whose sum is greater than or equal to the target.
# If no such subarray exists, return 0.

class Solution:
    def VariableLength(self, num: List[int]) -> int:
        l = 0
        r =0
        n = len(num)
        target = 4
        sum_num = 0
        min_length = float('inf')

        for r in range(n):
            sum_num += num[r]
            while sum_num >= target:
                min_length = min(min_length, r - l + 1)
                sum_num -= num[l]
                l += 1
        return min_length if min_length != float('inf') else 0
'''
Example:
num = [1,2,3]

r = 0
First sum = 1 <= 4

r =1
Second sum = 1+2 = 3 <= 4

r = 2
Third sum = 3 + 3 = 6 <= 4
min_length = (inf, 2 -0 + 1)
min_length = 3

sum_num -= num[0] -> 6 - 1 = 5
l += 1 -> l = 1

since sum_num = 5 and 5 >= 4
redo the process again

min_lenght = (3, 2 -1 + 1) = 2
min_length = 2
sum_num -= num[1] -> 5 - 2 = 3

sum = 3 and 3 < 4

Hence min_length = 2

Time complexity = O(n)
Space complexity = O(1)
'''

class Solution2:
    def VariableLength(self, num: List[int]) -> int:
        l = 0
        r = 0
        n = len(num)
        target = 4
        sum_num = 0
        set_num = set()

        for r in range(n):
            sum_num += num[r]
            while sum_num >= target:
                set_num.add(r -l + 1)
                sum_num -= num[l]
                l += 1
        return len(set_num)  if len(set_num) else 0

# Time Complexity of O(n)
# Space Complexity of O(n)

