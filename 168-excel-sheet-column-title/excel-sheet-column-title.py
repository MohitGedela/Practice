class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

        sequence = ""

        if (columnNumber - 1 <= 25):
            return letters[columnNumber - 1]
        
        else:
            while (columnNumber > 0):

                columnNumber -= 1

                index = columnNumber % 26

                sequence = letters[index] + sequence

                columnNumber //= 26

        return sequence

