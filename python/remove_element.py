class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x = [i for i in nums if i != val]
        nums[0:len(x)] = x
        return len(x)
