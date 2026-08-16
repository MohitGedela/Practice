class Solution:
    def addBinary(self, a: str, b: str) -> str:

        i = len(a) - 1
        j = len(b) - 1

        carry = 0
        result = ''

        while i >= 0 or j >=0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])

            if j >= 0:
                total += int(b[j])

            if total == 0:
                result = '0' + result
                carry = 0
            elif total == 1:
                result = '1' + result
                carry = 0
            elif total == 2:
                result = '0' + result
                carry = 1
            elif total == 3:
                result = '1' + result
                carry = 1

            i -= 1
            j -= 1

        return result