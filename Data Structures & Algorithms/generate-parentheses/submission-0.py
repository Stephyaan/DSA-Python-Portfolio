class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #valid if open==close
        #only add open if open<n
        #only add closing if,close count>open count -> valid

        res=[]
        stack=[]

        def backtrack(openN,closedN):
            if openN==closedN==n:
                res.append("".join(stack)) #n pairs obtained->append to res
                return

            if openN<n:  #n not reached
                stack.append('(')
                backtrack(openN+1,closedN) #increment the openN count, and call again
                stack.pop() #update stack;remove recent added

            if closedN<openN:  #closed to be added for pairs
                stack.append(')')
                backtrack(openN,closedN+1) #increment the closed count and call fn again
                stack.pop()  #update stack ; remove recently added


        backtrack(0,0)
        return res



        #for n pair,total n*2 parenthesis
        #n open and n close parenthesis