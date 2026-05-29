'''here are n cars traveling to the same destination on a one-lane highway.You are given two arrays of integers position and speed, both of length n.
position[i] is the position of the ith car (in miles), speed[i] is the speed of the ith car (in miles per hour), The destination is at position target miles.
A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.
A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.
If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.
Return the number of different car fleets that will arrive at the destination.'''
'''Algorithm
Pair each car's position with its speed.
Sort the cars in descending order of position (closest to target first).
For each car:
    Compute the time it takes to reach the target.
    Push this time onto a stack.
    If the new car’s time is less than or equal to the time before it,
    it catches up and merges with that fleet → pop it from the stack.
The number of remaining times in the stack equals the number of fleets.
Return the stack size.
'''
sol:
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair=[(p,s) for p,s in zip(position,speed)]
        stack=[]
        pair.sort(reverse=True)  #Reverse sorted order(to get highest in top)
        for p,s in pair: 
            stack.append((target-p)/s) 
            if (len(stack)>=2) and (stack[-1]<=stack[-2]): #current top(new car) time >= car b4 it(prev top)
                stack.pop()            #less time, then pop it, bcz next car merges with it
            
        return len(stack)
        
#time: O(nlogn) ; O(n) for operation, but sorting included so O(log n) 
#space: O(n)
