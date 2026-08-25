class Solution:
    def checkDivisibility(self, n: int) -> bool:

        sum = 0
        product = 1

        n = str(n)

        for i in range(len(n)):
            sum += int(n[i])
            product *= int(n[i])

        if int(n) % (sum + product) == 0:
            return True
        else:
            return False
        