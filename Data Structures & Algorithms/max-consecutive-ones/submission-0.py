class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max1 = 0 
        count = 0 

        for x in range(len(nums)):
            if nums[x] == 1:
                count += 1 
            else:
                if max1 < count:
                    max1 = count
                count = 0 

        if max1 < count:
            max1 = count

        return max1  