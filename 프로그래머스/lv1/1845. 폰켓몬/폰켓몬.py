def solution(nums):
    arr = set(nums)
    limit = len(nums) / 2
    
    if len(arr) >= limit:
        return limit
    elif len(arr) < limit:
        return len(arr)