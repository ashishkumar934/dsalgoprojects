from typing import List


def select_pivot_element(elements_list: List[int]) -> (int, int):
    # Returning the first element of the array as the pivot
    pivot = elements_list[0]
    index = 0
    return pivot, index


def partition(elements_list: List[int], pivot: int, pivot_index: int) -> (List[int], List[int]):
    left_elements_list = []
    right_elements_list = []
    for i in range(len(elements_list)):
        if i == pivot_index:
            continue
        elif elements_list[i] > pivot:
            right_elements_list.append(elements_list[i])
        elif elements_list[i] <= pivot:
            left_elements_list.append(elements_list[i])

    return left_elements_list, right_elements_list


def inplace_partition(elements_list: List[int], pivot: int, pivot_index: int) -> (List[int], List[int]):
    left = 0
    right = len(elements_list)-1

    while left < right:
        while elements_list[left] <= pivot:
            left += 1
        while elements_list[right] > pivot:
            right -= 1
        if left < right:
            elements_list[left], elements_list[right] = elements_list[right], elements_list[left]



def quick_sort(elements_list: List[int]) -> List[int]:
    print('calling the quick sort algo')
    if len(elements_list) == 0:
        return elements_list
    pivot, pivot_index = select_pivot_element(elements_list)
    left_elements_list, right_elements_list = partition(elements_list, pivot, pivot_index)
    sorted_left_elements_list = quick_sort(left_elements_list)
    sorted_right_elements_list = quick_sort(right_elements_list)
    elements_list = sorted_left_elements_list + [pivot] + sorted_right_elements_list
    return elements_list


if __name__ == '__main__':
    given_list = [1, 3, 4, 5, 6, 7, 8, 2, 45, 1, 3, 67, 8, 9, 332, 12, 443, 343, 323]
    print(quick_sort(given_list))
