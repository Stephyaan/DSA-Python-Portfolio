#Time: O(logn) ; Space : O(1)
'''n asked specifically time complexity of O(logn) ; Binary search is optimal here '''
'''Algorithm
Initialize left = 0, right = n - 1, and store the first element as the current answer.
While left <= right:
If the current window is already sorted, update the answer with nums[left] and stop.
Compute mid.
Update the answer with nums[mid].
If the left half is sorted:
Move search to the right half.
Otherwise:
Search in the left half.
Return the smallest value found.
'''
Sol:
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
