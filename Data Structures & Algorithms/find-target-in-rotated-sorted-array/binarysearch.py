'''Algorithm
Use binary search to locate the pivot:
Compare middle and right elements.
If nums[mid] > nums[right], the pivot is to the right.
Otherwise, it's to the left (including mid).
After finding the pivot:
If the target lies between nums[pivot] and the last element, search the right half.
Otherwise, search the left half.
Perform a standard binary search on the selected half.
Return the index if found, else -1.'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

#time:O(log n)
#space: O(1)
