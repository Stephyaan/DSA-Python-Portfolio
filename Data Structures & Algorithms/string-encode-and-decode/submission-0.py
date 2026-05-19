class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=""
        for s in strs:
            encoded_string+=str(len(s))+"#"+s
        #return combined form with length(int)+# as delimeter preceeding the og string element
        return encoded_string


    def decode(self, s: str) -> List[str]:
        decoded_strs,i=[],0
        while i < len(s):
            j=i
            while s[j] != "#":
                j+=1        #j is finally at # position
            length=int(s[i:j])     #get the length(int) part of delimeter
            decoded_strs.append(s[(j+1):(j+1+length)]) #j+1=start of string, j+1+length=end of string
            i=j+1+length       #i incremented to end of string to get the next string start           
        return decoded_strs
