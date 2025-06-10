def bubble_sort(arr):
    """
    Perform bubble sort on a list.

    :param arr: List of elements to be sorted.
    :return: Sorted list.
    """
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def quick_sort(arr, pivot_strategy='middle'):
    """
    Perform quick sort on a list with customizable pivot selection strategy.

    :param arr: List of elements to be sorted.
    :param pivot_strategy: Strategy for selecting pivot element.
                          Options: 'first', 'last', 'middle', 'random', 'median_of_three'.
    :return: Sorted list.
    """
    import random
    
    if len(arr) <= 1:
        return arr
    
    # 选择基准元素
    if pivot_strategy == 'first':
        pivot = arr[0]
    elif pivot_strategy == 'last':
        pivot = arr[-1]
    elif pivot_strategy == 'middle':
        pivot = arr[len(arr) // 2]
    elif pivot_strategy == 'random':
        pivot = arr[random.randint(0, len(arr) - 1)]
    elif pivot_strategy == 'median_of_three':
        first = arr[0]
        middle = arr[len(arr) // 2]
        last = arr[-1]
        # 找出三个元素的中位数
        if first <= middle <= last or last <= middle <= first:
            pivot = middle
        elif middle <= first <= last or last <= first <= middle:
            pivot = first
        else:
            pivot = last
    else:
        # 默认使用中间元素作为pivot
        pivot = arr[len(arr) // 2]
    
    # 分割数组
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # 递归排序并合并结果
    return quick_sort(left, pivot_strategy) + middle + quick_sort(right, pivot_strategy)
