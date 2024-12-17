import math_problems
#  bubble sort


def bubble_sort(numbers, is_log=False):  # 預設不印
    for round in range(len(numbers)-1):
        for index in range(len(numbers)-1-round):
            if numbers[index] > numbers[index+1]:
                numbers[index], numbers[index+1] = \
                    numbers[index+1], numbers[index]
        if is_log:
            print(round, numbers)
    return numbers

# selection sort


def selection_sort(numbers, is_log=False):
    for round in range(len(numbers)-1):
        min_index = round
        for index in range(round+1, len(numbers)):
            if numbers[index] < numbers[min_index]:
                min_index = index
        if min_index != round:
            numbers[round], numbers[min_index] = numbers[min_index], numbers[round]
        if is_log:
            print(round, numbers)
    return numbers


if __name__ == "__main__":
    nums = [40, 50, 60, 30, 10]
    print(bubble_sort(nums))
    print("ABC")
else:
    print("ABC", __name__)
print('結束')
