#Given an array of integers and a number k, find the maximum sum of any contiguous subarray of size k.
class FixedLength:
    def Solution(self, arr: List[int], k=3) -> int:
        n = len(arr)
        sum_arr = 0

        for i in range(k):
            sum_arr += arr[i]

        max_sum = sum_arr

        for i in range(k, n):
            sum_arr += arr[i]
            sum_arr -= arr[i-k]
            max_sum = sum_arr

        max_sum = max(max_sum, sum_arr)
        return max_sum

# Time complexity : O(n)
# Space complexity : O(1)