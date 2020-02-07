from typing import List

arr = [-5, -2, 15, -2, 10, 6, 12, 8, 15,
       15, 17, 18, 7, 20, 10, 15, -3, 4, 3, 3]


def find_peak(arr: List[int]) -> (int, int):
    for i in range(len(arr)):

        if i == 0:
            if arr[i] >= arr[i+1]:
                return (i, arr[i])

        if i == len(arr):
            if arr[i] >= arr[i-1]:
                return (i, arr[i])

        if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
            return (i, arr[i])

    return (-1, -1)


if __name__ == "__main__":
    idx, val = find_peak(arr)
    print("IDX:{} - VAL:{}".format(idx, val))
