# Valid Anagram: Given two string s and t, return true if t is an anagram of s, and false otherwise

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n, k = len(s), len(t)
        if n != k:
            return False

        countS, countT = {}, {}

        for i in range(n):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)


        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True

"""
Time complexity: O(n)
Space Complexity: O(n)

anagram = Solution()
print(anagram.isAnagram("lust", "slut"))
"""