nums = [-1,0,0,0,0,3,3]
def find_duplicates(nums):
    singles_len = 0
    nums_len = len(nums)
    
    if len(nums) <= (3*(10**4)) and len(nums)>0:
        singles = set()
        for i in nums:
            singles.add(i)
        counter = 0
        singles_len = len(singles)
        for i in nums:
            if len(singles) > 0:
                nums[counter] = singles.pop()
            else:
                nums[counter] = "_"
            counter += 1
        
        nums[0:singles_len] = sorted(nums[0:singles_len])
        print(nums)
            
    elif nums_len == 0:
        nums = [0]


    return singles_len

find_duplicates(nums)