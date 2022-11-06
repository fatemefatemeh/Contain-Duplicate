def ContainDuplicate(nums):
    c=[]
    for i in nums:
        c.append(nums.count(i))
    
    print(set(c))

    for i in c:
        if i >=2:
            return True
        
    return  False


nums=[1,2,5,7,2,5,2]
print(ContainDuplicate(nums))