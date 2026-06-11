class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp = []
        for x in nums:
            if x == val:
                continue 
            temp.append(x)
        for i in range(len(temp)):
            nums[i] = temp[i]
        return len(temp)