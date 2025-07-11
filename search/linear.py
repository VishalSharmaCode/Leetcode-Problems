def linearSearch(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return 'Element is not in this array'
        
print('Position of element is:>', linearSearch([1,2,3,4,5], 10))