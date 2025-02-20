def selection_sort(nums):
    for i in range(len(nums)):
        min_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums

def quickSort(arry):
    if len(arry) <= 1:
        return arry
    pivot = arry[0]
    inf_pivot = [i for i in arry[1:] if i<pivot]
    sup_pivot = [i for i in arry[1:] if i>pivot]
    return quickSort(inf_pivot)+[pivot]+quickSort(sup_pivot)

def quick_sort(nums, low, high):
    if low >= high:
        return nums
    i = partitions(nums , low, high)
    quick_sort(nums, 0, i-1)
    quick_sort(nums, i+1, high)
    return nums
def partitions(nums, low, high):
    pivot = nums[high]
    i = low
    for j in range(low, high):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[high] = nums[high], nums[i]
    return i


def bubble_sort(nums):
    swapping = True
    end = len(nums)
    while swapping:
        swapping = False
        for i in range(end - 1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                swapping = True
        end -= 1
    return nums

def merge_sort(nums):
    if len(nums)<=1:
        return nums
    return merge(merge_sort(nums[:len(nums)//2]), merge_sort(nums[len(nums)//2:]))
def merge(nums_1, nums_2):
    final = []
    i, j = 0, 0
    while i <= (len(nums_1)-1) and j <= (len(nums_2)-1):
        if nums_1[i] <= nums_2[j]:
            final.append(nums_1[i])
            i += 1
        else:
            final.append(nums_2[j])
            j += 1
    final += nums_1[i:] if i < len(nums_1) else nums_2[j:]
    return final

def insertSort(nums):
    for i in range(1, len(nums)):
        j = i -1
        while j >= 0:
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
            j -= 1
    return nums

def binarySearch(arry, target):
    if len(arry) <1:
        return None
    low=0
    high=len(arry)-1
    while low<=high:
        mid=(low+high)//2
        if arry[mid] == target:
            return True
        if arry[mid]<target:
            low=mid+1
        if arry[mid]>target:
            high=mid-1
    return False

if __name__ == "__main__":
    arry = [23, 87, 15, 92, 44, 78, 36, 11, 55, 90, 62, 5, 31, 74, 98, 20, 66, 47, 83, 29]
    result = selection_sort(arry)
    print(result)
    print("list sorted")
    search = binarySearch(result, 78)
    print(search)
    print(binarySearch([2], 79))
    print(binarySearch([], 79))
