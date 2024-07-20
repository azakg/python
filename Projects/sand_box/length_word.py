class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Assume the first string is the prefix
        prefix = strs[0]

        # Compare the prefix with each string
        for s in strs[1:]:
            while not s.startswith(prefix):
                # Shorten the prefix by one character
                prefix = prefix[:-1]
                # If the prefix is empty, return ""
                if not prefix:
                    return ""

        return prefix

object1 = Solution()
strs = ["flower","flow","flight"]
print(object1.longestCommonPrefix(strs))