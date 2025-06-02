class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target
        self.output = []

        for index,num in enumerate(self.nums):
            if num == self.nums[-1]:
                print("ran till last index")
                pass
            elif self.nums[index] + self.nums[index + 1] == target:
                print(f"{self.nums[index]} + {self.nums[index + 1]}")
                self.output.append(index)
                self.output.append(index+1)
        return self.output
c = Solution()
c.twoSum([2,7,11,15],9)   