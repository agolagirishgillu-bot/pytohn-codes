class pair_element:
    def twoword(self,nums,target):

        lookup={}

        for i,num in enumerate(nums):
            if target-nums in lookup:
                return (lookup[target-num],i)

