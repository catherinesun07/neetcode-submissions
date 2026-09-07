class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        maxL = 0
        result = ""

        i = 0 

        while i < length and (i + maxL/2 -2) < length:
            left = right = i
            odd=""
            while left >= 0 and right < length and s[left] ==s[right]:
                odd = s[left:right+1]
                left -=1
                right +=1
            l = i
            r = i +1 
            even = ""
            while l >= 0 and r < length and s[l] ==s[r]:
                even = s[l:r+1]
                l-=1
                r+=1
            
            if len(odd) > maxL:
                result = odd
                maxL = len(odd)
            if len(even) > maxL:
                result = even
                maxL = len(even)
            i+=1
            
            
        
        return result

            


