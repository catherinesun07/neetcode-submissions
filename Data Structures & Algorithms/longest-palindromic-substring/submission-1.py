class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        maxL = 0
        start = 0

        i = 0 

        while i < length and (i + maxL/2 -2) < length:
            left = right = i
            currL = 0
            while left >= 0 and right < length and s[left] ==s[right]:
                left -=1
                right +=1
            currL = right - left - 1
            if currL > maxL:
                maxL = currL
                start = left +1
            
            left = i
            right = i + 1
            while left >= 0 and right < length and s[left] ==s[right]:
                left -=1
                right +=1
            currL = right - left - 1
            if currL > maxL:
                maxL = currL
                start = left +1 
            i+=1
        
        return s[start: start+maxL]

            


