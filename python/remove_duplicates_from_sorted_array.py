class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = list(set(nums))
        x.sort()
        nums[0:len(x)] = x
        return len(x)
