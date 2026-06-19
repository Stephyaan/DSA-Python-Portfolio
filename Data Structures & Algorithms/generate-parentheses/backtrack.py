'''You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.
Example 2: Input: n = 3 ; Output: ["((()))","(()())","(())()","()(())","()()()"]'''
'''algorithm:
create the resulting array
create stack to store the parenthesis added
define recursion fn. backtrack(openN,closeN):
    check if no.of closed and open parenthesis equals given n:
        then,join the elements in stack,and append to res
        return
    check count of open parenthesis<n:
        append ( to stack
        continue recusrsion function with updated count, openN+1
        (remove the last element from stack and update)
    check count of closed parenthesis > n:
        append ) to stack
        continue recursion with new count of closedN+1
        (pop the recent element from stack)
'''backtrack after each choice

call from start backtrack(0,0)
return res
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #for n pair,total n*2 parenthesis
        #n open and n close parenthesis
        res=[]
        stack=[]

        def backtrack(openN,closedN):
            #valid if open==close
            if openN==closedN==n:
                res.append("".join(stack)) #n pairs obtained->append to res
                return

            #only add open if open<n
            if openN<n:  #n not reached
                stack.append('(')
                backtrack(openN+1,closedN) #increment the openN count, and call again
                stack.pop() #update stack;remove recent added

            #only add closing if,close count>open count -> valid
            if closedN<openN:  #closed to be added for pairs
                stack.append(')')
                backtrack(openN,closedN+1) #increment the closed count and call fn again
                stack.pop()  #update stack ; remove recently added


        backtrack(0,0)
        return res
#time:O(4^n/root n)
#space:O(n)
