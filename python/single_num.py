class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = []
        for num in nums:
            if num not in x:
                x.append(num)
                nums.remove(num)
        for i in x:
            if i not in nums:
                return i
