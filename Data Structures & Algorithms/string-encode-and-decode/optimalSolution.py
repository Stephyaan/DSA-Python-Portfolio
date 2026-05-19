#Algorithm
#Encoding
#Initialize an empty result string.
#For each string in the list:
#Compute its length.
#Append "length#string" to the result.
#Return the final encoded string.

#Decoding
#Initialize an empty list for the decoded strings and a pointer i = 0.
#While i is within the bounds of the encoded string:
#Move a pointer j forward until it finds '#' — this segment represents the length.
#Convert the substring s[i:j] into an integer length.
#Move i to the character right after '#'.
#Extract the next length characters — this is the original string.
#Append the extracted string to the result list.
#Move i forward by length to continue decoding the next segment.
#Return the list of decoded strings.

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

#Time complexity: O(m) for each encode() and decode() function calls.
#Space complexity: O(m+n) for each encode() and decode() function calls.
