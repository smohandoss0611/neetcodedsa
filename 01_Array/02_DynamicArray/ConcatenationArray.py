from typing import List
class Solution:
    def concatenationarray(self, nums : List[int]) ->  List[int]:
        concatenated = nums + nums 
        return concatenated
s = Solution()
nums =[1,3,3]
output = s.concatenationarray(nums)
print(output)