from typing import List, Union, Any


def partition(elements_list: List[int], pivot: int, pivot_index: int) -> int:
    left = 0
    right = len(elements_list) - 1

    while left <= right:
        while elements_list[left] <= pivot:
            left += 1
            if left >= len(elements_list):
                break
        while elements_list[right] > pivot:
            right -= 1
            if right < 0:
                break
        if left < right:
            elements_list[left], elements_list[right] = elements_list[right], elements_list[left]

    # Move pivot to its final position
    elements_list[left], elements_list[pivot_index] = elements_list[pivot_index], elements_list[left]
    print(elements_list)
    return left


def inplace_partition(elements_list: List[int], pivot: int, pivot_index: int) -> int:
    left = 0
    right = len(elements_list) - 1

    while left <= right:
        while left <= right and elements_list[left] < pivot:
            left += 1
        while left <= right and elements_list[right] > pivot:
            right -= 1
        if left <= right:
            elements_list[left], elements_list[right] = elements_list[right], elements_list[left]
            left += 1
            right -= 1

    # Move pivot to its final position
    elements_list[left], elements_list[pivot_index] = elements_list[pivot_index], elements_list[left]
    print(elements_list)
    return left


if __name__ == '__main__':
    given_list: List[Union[int, Any]] = [70, 1, 2, 3, 100, 4, 69, 71, 300, 400, 7]
    print(partition(given_list, 70, 0))
    print(inplace_partition(given_list, 70, 0))
