#Qn: You are given a string s consisting of only uppercase english characters and an integer k. 
You can choose up to k characters of the string and replace them with any other uppercase English character.
After performing at most k replacements, return the length of the longest substring which contains only one distinct character.
#algorithm:
#Create a frequency map count and initialize left pointer,l = 0, maxf = 0, and size of longest substring,res = 0.
#Move the right pointer r across the string through loop:
    #Update the frequency of s[r].
    #Update maxf with the highest frequency seen so far.
#If the window size, (r-l-1), is invalid (window size - maxf > k):
    #Shrink the window from the left and adjust counts.
#Update the result with the valid window size.
#Return res at the end.
    
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        l=0
        res=0
        maxf=0
        for r in range(len(s)):
            count[s[r]]=1+count.get(s[r],0)  #0 if s[r] not in count{}
            maxf=max(maxf,count[s[r]])

            while ((r-l+1)-maxf) >k:    #invalid window size, valid only if (r-l+1)-maxf <= k
                count[s[l]]-=1          
                l+=1
            res=max(res,r-l+1)  #valid window size
        return res

#time:O(n*m)
#space:O(m)
        
