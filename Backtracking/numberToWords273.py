class Solution:
    def numberToWords(self, num: int) -> str:
        # 0 <= num <= 2**31 - 1 = 2,147,483,647 (2 billion)
        self.lessThan20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        self.tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        self.thousands = ["","Thousand","Million","Billion"]

        if num == 0:
            return "Zero"
        
        res = ""
        for i in range(len(self.thousands)):
            if num % 1000 != 0:
                # split by 3 digits as a group, recursion from left to right
                # 12345 -> helper(12) + helper(345)
                # 1234567 -> helper(1) + helper(234) + helper(567)
                res = self.helper(num % 1000) + self.thousands[i] + " " + res
            num //= 1000
        return res.strip()

    def helper(self, num):
        # num <= 999
        if num == 0:
            return ""
        elif num < 20:
            return self.lessThan20[num] + " "
        elif num < 100:
            return self.tens[num // 10] + " " + self.helper(num % 10)
        else:
            return self.lessThan20[num // 100] + " Hundred " + self.helper(num % 100)