def sortArray(self, nums):
        n=(len(nums))
        for i in range(n-1):
            min_index =i
            for j in range(i,n):
                if(nums[j] < nums[min_index]):
                    min_index = j
            nums[i],nums[min_index] = nums[min_index],nums[i]
        return nums 
nums=[3,2,4,1,0]
print(sortArray(nums))
        