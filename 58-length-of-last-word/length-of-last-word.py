class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = s.split(" ")
        i = len(result) - 1

        while True:
            if result[i] == "":
                i -= 1
                continue
            else:
                return len(result[i])
        