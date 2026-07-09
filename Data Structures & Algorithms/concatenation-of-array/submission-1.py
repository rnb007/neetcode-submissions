class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        output_arr = nums.copy()
        for i in output_arr:
            nums.append(i)

        return nums