class Solution:
    def isPalindrome(self, x: int) -> bool:

        num = str(x)

        number = int(0)

        if len(num) % 2 == 0 :
            number = len(num)/2
        else :
            number = (len(num)-1)/2

        
        truthCount = True


        for i in range(int(number)):
            if num[i] == num[len(num)-i-1]:
                truthCount = True
            else:
                truthCount = False
                break

        return truthCount