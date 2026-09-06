class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        count =0

        for i in range(length):
            #center expand
            l = i  
            r = i
            while l>=0 and r<length and s[l] == s[r]:
                count +=1
                l -=1
                r +=1
               
            #even expansion
            left = i
            right = i+1
            while left>=0 and right<length and s[left] == s[right]:
                count +=1
                left -=1
                right +=1
        
        return count
        