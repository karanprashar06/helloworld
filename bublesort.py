def sort(nums):
    for i in range (len(nums)-1,0,-1):
        for j in range(i):
             if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp

nums=[12,34,23,55,232,121,55]
print(nums.count(232))
sort(nums)

print(nums)