#Algorithm
#Create a hash map where each key is the sorted version of a string, and the value is a list of strings belonging to that anagram group.
#Iterate through each string in the input list:
#Sort the characters of the string to form a key.
#Append the original string to the list corresponding to this key.
#After processing all strings, return all values from the hash map, which represent the grouped anagrams.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)  #. It automatically creates an empty list ([]) as the value whenever you access a key that doesn't exist yet. 
        for s in strs:
            sortedS=''.join(sorted(s))  #sorted(s): The built-in sorted() function takes the string s and breaks it into a list of individual characters, 
                                         #then sorts them (e.g., "cba" becomes ['a', 'b', 'c']).
                                         #''.join(...): The join() method takes that list of characters and stitches them back together into a single string, 
                                        #using an empty string '' as the separator.
            result[sortedS].append(s)
        return list(result.values())

#time: O(m*nlogn) m=no.of strings in array,n=avg length of string
#space: O(m*n)
