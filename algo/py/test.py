def quickSort(arry):
    if len(arry) <= 1:
        return arry
    pivot = arry[0]
    inf_pivot = [i for i in arry[1:] if i<pivot]
    sup_pivot = [i for i in arry[1:] if i>pivot]
    return quickSort(inf_pivot)+[pivot]+quickSort(sup_pivot)
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
    result = quickSort(arry)
    print(result)
    search = binarySearch(result, 79)
    print(search)
    print(binarySearch([2], 79))
    print(binarySearch([], 79))
