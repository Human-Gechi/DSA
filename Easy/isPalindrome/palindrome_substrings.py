
class SolutionLongest:
    def lenPalindrome(self, string: str) -> int:
        if not string:
            return 0

        n = len(string)
        best_len = 1

        for i in range(n):
            left = i
            right = i
            while left >= 0 and right < n and string[left] == string[right]:
                best_len = max(best_len, right - left + 1)
                left -= 1
                right += 1

            left = i
            right = i + 1
            while left >= 0 and right < n and string[left] == string[right]:
                best_len = max(best_len, right - left + 1)
                left -= 1
                right += 1

        return best_len


# Space complexity = O(1)