class Solution:
    def minimumPushes(self, word: str) -> int:

        freq = {}

        for char in word:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        frequencies = list(freq.values())
        frequencies.sort(reverse=True)


        total = 0

        for i in range(len(frequencies)):
            if i < 8:
                pushes = 1
            elif i < 16:
                pushes = 2
            elif i < 24:
                pushes = 3
            else:
                pushes = 4

            total += frequencies[i] * pushes

        return total
