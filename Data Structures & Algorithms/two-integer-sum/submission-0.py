class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def array(num,target):
            for i in range(len(num)):
                for j in range(i+1,len(num)):
                    if(num[i]+num[j]==target):
                        return([i,j])

        return array(nums, target)
        