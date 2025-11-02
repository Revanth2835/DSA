def searchRange( nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        if l >= len(nums) or nums[l] != target:
            return [-1, -1]
        left = l
        
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        right = r
        
        return [left, right]