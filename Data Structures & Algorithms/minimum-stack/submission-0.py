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
        
