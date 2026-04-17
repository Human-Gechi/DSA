"""
Valid Palindrome
Easy
Topics
Company Tags
Hints
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        left = 0
        right = len(res) -1

        while left < right:
            if res[left] != res[right]:
                return False
            left += 1
            right -= 1

        return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) -1

        while left < right:
            if s[left].isalnum():
                if s[right].isalnum():
                    if s[left].lower() != s[right].lower():
                        return False
                    left += 1
                    right -=1
                else:
                    right -= 1
            else:
                left += 1

        return True

"""
First solution
Time complexity: O(n)
Space complexity: O(n)

Second solution
Time complexity: O(n)
Space complexity: O(1)
"""