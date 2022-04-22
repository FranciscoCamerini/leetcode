class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        _ = [str(i) for i in digits]
        digits = int(''.join(_))
        digits += 1
        digits = list(str(digits))
        return digits
