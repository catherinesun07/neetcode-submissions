class Solution:
    def countSubstrings(self, s: str) -> int:
        count =0

        for i in range(0,len(s)):
            #center expand
            l = i  
            r = i
            while l>=0 and r<len(s):
                if s[l] == s[r]:
                    count +=1
                    l -=1
                    r +=1
                else: 
                    break
            #even expansion
            left = i
            right = i+1
            while left>=0 and right<len(s):
                if s[left] == s[right]:
                    count +=1
                    left -=1
                    right +=1
                else:
                    break

        return count
        