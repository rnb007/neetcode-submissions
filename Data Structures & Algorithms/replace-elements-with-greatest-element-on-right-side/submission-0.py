class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        def max_no(nums):

            max_number = 0

            for i in nums:
                if i>max_number:
                    max_number = i
            
            return max_number

        output = []
        for i in range(len(arr)-1):
            output.append(max_no(arr[i+1:]))
        
        output.append(-1)
        
        return output

        