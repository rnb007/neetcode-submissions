class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        removed_list = []

        for i in nums:
            if i != val:
                removed_list.append(i)
                
        k = len(removed_list)
        
        for i in range(k):
            nums[i] = removed_list[i]
        
        return k

        