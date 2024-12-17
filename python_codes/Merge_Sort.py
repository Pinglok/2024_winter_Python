def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if len(left) > 0:
        result += left
    else:
        result += right
    return result


def merge_sort(numbers):
    if len(numbers) == 1:
        return numbers
    else:
        mid_index = len(numbers) // 2
        left_part = numbers[:mid_index]
        right_part = numbers[mid_index:]
        sorted_left_part = merge_sort(left_part)
        sorted_right_part = merge_sort(right_part)
        return merge(sorted_left_part, sorted_right_part)


if __name__ == "__main__":
    numbers = [20, 40, 50, 10, 60, 90, 80, 70, 30]
    result = merge_sort(numbers)
    print(result)
