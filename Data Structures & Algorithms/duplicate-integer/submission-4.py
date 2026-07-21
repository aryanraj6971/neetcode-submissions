class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        def array(nums):
            hash_map={}
            
            for i in range(len(nums)):
                compliment=nums[i]
                if compliment in hash_map:
                    return True
                hash_map[nums[i]]=i

            
            return False

        return(array(nums))
    