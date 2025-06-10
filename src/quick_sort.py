def quick_sort(arr):
    """
    Perform quick sort on a list.

    :param arr: List of elements to be sorted.
    :return: Sorted list.
    """
    if len(arr) <= 1:
        return arr
    
    # 选择基准元素
    pivot = arr[len(arr) // 2]
    
    # 分割数组
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # 递归排序并合并结果
    return quick_sort(left) + middle + quick_sort(right)
