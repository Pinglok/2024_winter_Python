import random

# 随机选择10个不重复的元素
numbers = random.choices(range(100), k=10)
numbers = sorted(numbers)

print(numbers)
target = random.choice(numbers)  # 随机选择一个目标元素
print(target)


start = 0
end = len(numbers) - 1
while start <= end:
    mid = (start + end) // 2
    mid_value = numbers[mid]
    if mid_value < target:
        start = mid + 1
    elif mid_value > target:
        end = mid - 1
    else:
        print('find target at', mid)
        break
# else:
#    print('target not found')

print('Target:', target)
