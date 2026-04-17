class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [""]
        output = {}

        for word in strs:
            count = [0] * 26 # count for each word
            for char in word:
                count[ord(char) - ord('a')] += 1

            key = tuple(count)
            output.setdefault(key, []).append(word)

        return list(output.values())

"""
dictionr
Space complexity : O(n)

Time complexity : O(n * k)

anagram = Solution()
print(anagram.groupAnagrams(["lust", "slut","pot", "top", "tip", "pit", ""]))
"""
