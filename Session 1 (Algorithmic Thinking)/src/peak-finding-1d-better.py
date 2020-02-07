from typing import List

arr = [-5, -2, 15, -2, 10, 6, 12, 8, 15,
       15, 17, 18, 7, 20, 10, 15, -3, 4, 3, 3]


def find_peak(arr: List[int]) -> (int, int):
    midx = int(len(arr)/2)
    if arr[midx] >= arr[midx-1] and arr[midx] >= arr[midx+1]:
        return (midx, arr[midx])

    if arr[midx] < arr[midx+1]:
        return find_peak(arr[:midx-1])

    if arr[midx] < arr[midx-1]:
        return find_peak(arr[midx+1:])

    return (-1, -1)


if __name__ == "__main__":
    idx, val = find_peak(arr)
    print("IDX:{} - VAL:{}".format(idx, val))
