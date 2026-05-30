'''O(logn) Case''' ''' Space: O(1)'''
'''Algorithm:
Initialize two pointers:
l = 0 (start of array)
r = len(nums) - 1 (end of array)
While l <= r:
Compute m = l + (r - l) // 2 (safe midpoint).
If nums[m] == target, return m.
If nums[m] < target, move search to the right half: update l = m + 1.
If nums[m] > target, move search to the left half: update r = m - 1.
If the loop ends without finding the target, return -1.
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            #loop till target==nums[mid]
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1
