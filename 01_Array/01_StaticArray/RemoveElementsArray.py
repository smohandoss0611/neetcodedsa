from typing import List
class Solution(object):
    def RemoveElementsFromArray(self, nums : List[int], val: int) -> int:
        l = 0
        for r in range(0,len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l = l + 1
        return l
    
def main():
    obj = Solution()
    nums =[1,32,3,4,5]
    output = obj.RemoveElementsFromArray(nums,32)
    print(f"Length of the Array:{output}")
    print(f"Array: {nums[:output]}")

if __name__ =="__main__":
    main()  
