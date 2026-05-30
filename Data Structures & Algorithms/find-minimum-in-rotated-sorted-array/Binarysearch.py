#Time: O(logn) ; Space : O(1)
'''n asked specifically time complexity of O(logn) ; Binary search is optimal here '''
'''Algorithm
Set left = 0 and right = n - 1.
While left < right:
Compute mid.
If nums[mid] is less than nums[right], move right to mid (minimum is on the left).
Otherwise, move left to mid + 1 (minimum is on the right).
When the loop ends, left points to the smallest element.
Return nums[left].
'''
Sol:
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]
