from typing import List
class Solution(object):
  def removeDuplicates(self, nums: List[int]) -> int:
       l = 1
       for  r in  range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
       return l
  
def main():
    sol = Solution()
    nums = [1,1,2,2,3,3,4,4,5]
    length  = sol.removeDuplicates(nums)
    print(f"Length of array after removing duplicates:{length}")
    print(f"Array after removing duplicates:{nums[:length]}")

if __name__ =="__main__":
    main()  
  

            

            
