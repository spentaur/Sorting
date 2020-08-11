# %%
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    i, j, k = 0, 0, 0

    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            i += 1
        else:
            merged_arr[k] = arrB[j]
            j += 1

        k += 1

    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i += 1
        k += 1

    while j < len(arrB):
        merged_arr[k] = arrB[j]
        j += 1
        k += 1

    return merged_arr


# %%


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        arr = merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

    return arr

# %%


def merge_in_place(arr, start, mid, end):

    return arr


def merge_sort_in_place(arr, l, r):

    return arr


def timsort(arr):

    return arr


# %%
