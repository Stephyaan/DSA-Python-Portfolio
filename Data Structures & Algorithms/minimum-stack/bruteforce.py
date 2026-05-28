'''Qn: Design a stack class that supports the push, pop, top, and getMin operations.MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
Each function should run in O(1) time.
'''
'''Algorithm:
To push a value, append it to the stack.
To pop, remove the top element of the stack.
To top, return the last element.
To getMin:
Create a temporary list.
Pop all elements from the stack while tracking the smallest value.
Push all elements back from the temporary list to restore the stack.
Return the smallest value found.
'''
sol:
class MinStack:

    def __init__(self):
        self.stack=[]  #initialize self stack 

    def push(self, val: int) -> None:
        self.stack.append(val) #push val to stack;becomes top,last element entered

    def pop(self) -> None:
        self.stack.pop()  #pops/removes last element pushed to stack,top

    def top(self) -> int:
        return self.stack[-1]  #top=last element in stack(entered)

    def getMin(self) -> int:
        tmp=[]  #temp list 
        mini=self.stack[-1]  #keep track of min in stack;starts from top/last element
        
        #track through each element(by popping top) to update mini to smallest value
        while len(self.stack): 
            mini=min(mini,self.stack[-1]) #update mini with min(mini,updated top)
            tmp.append(self.stack.pop()) #pop top element to tmp;top updated

        while len(tmp):
            self.stack.append(tmp.pop())  #pop from tmp back to stack;we get in order

        return mini #return final mini obtained

#time:O(1) for all;getMin:O(n)
#space:O(n)
