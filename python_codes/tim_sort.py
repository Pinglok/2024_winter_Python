import random


def insert_sort(numbers):
    answer = []  # 定义 answer 变量
    for new in numbers:
        is_insert = False
        for index, num in enumerate(answer):  # enumerate 同時給你編號跟對應的值
            if new < num:
                answer.insert(index, new)
                is_insert = True
                break
        if not is_insert:
            answer.append(new)
    return answer


def merge(left, right):
    result = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result


def tim_sort(numbers):
    RUN = 32  # 设置 RUN 的值
    if len(numbers) <= RUN:
        return insert_sort(numbers)
    else:
        mid_index = len(numbers) // 2
        left_part = numbers[:mid_index]
        right_part = numbers[mid_index:]
        sorted_left_part = tim_sort(left_part)
        sorted_right_part = tim_sort(right_part)
        return merge(sorted_left_part, sorted_right_part)


if __name__ == '__main__':
    numbers = random.sample(range(10000), k=1024)
    result = tim_sort(numbers)
    assert result == sorted(numbers)
    print(result)
