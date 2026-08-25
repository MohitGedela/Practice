class Solution:
    def minimumPushes(self, word: str) -> int:
        
        counter = 0

        for i in range(len(word)):

            if i <= 7:
                counter += 1
            elif i <= 15:
                counter += 2
            elif i <= 23:
                counter += 3
            else:
                counter += 4

        return counter