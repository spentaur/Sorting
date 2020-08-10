def selection_sort(arr):
    # start with index = 0
    # for all indices except last
    for ii in range(len(arr)):
        minIdx = ii
        for jj in range(ii + 1, len(arr)):
            if arr[minIdx] > arr[jj]:
                minIdx = jj

        arr[ii], arr[minIdx] = arr[minIdx], arr[ii]

    return arr


def bubble_sort(arr):
    # loop through array
    for ii in range(len(arr)):
        for jj in range(len(arr) - 1):
            if arr[jj] > arr[jj + 1]:
                arr[jj], arr[jj + 1] = arr[jj + 1], arr[jj]

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
