class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        counter = 0
        string = ''

        if not strs or "" in strs:
            return ""
#
        if len(strs) == 1:
            return strs[0]

        while True:
            for i in range(len(strs) - 1):
                
                if counter >= len(strs[i]) or counter >= len(strs[i + 1]):
                    return string
                
                if strs[i][counter] != strs[i + 1][counter]:
                    return string

            string += strs[0][counter]
            counter += 1

        return string