
def insert_sort(numbers):
    answer = []  # 定义 answer 变量
    for new in numbers:
        is_insert = False
        for index, num in enumerate(answer):  # enumerate 同時給你編號跟對應邊烙的職
            if new < num:
                is_insert = True
                answer = answer[:index] + [new] + answer[index:]
                break
        if not is_insert:
            answer.append(new)
    return answer


num = [40, 30, 50, 60, 20]
answers = insert_sort(num)
print(answers)


answer = [40]
new = 30
if answer:
    is_insert = False
    for index, num in enumerate(answer):  # enumerate 同時給你編號跟對應邊烙的職
        if new < num:
            is_insert = True
            answer = answer[:index]+[new] + answer[index:]
            break
        else:
            answer = answer + [new]
else:
    answer = [new]
print(answer)

answer = [30]
new = 50
if answer:
    is_insert = False
    for index, num in enumerate(answer):  # enumerate 同時給你編號跟對應邊烙的職
        if new < num:
            is_insert = True
            answer = answer[:index]+[new] + answer[index:]
            break
        else:
            answer = answer + [new]
else:
    answer = [new]
print(answer)

answer = [50]
new = 20
if answer:
    is_insert = False
    for index, num in enumerate(answer):  # enumerate 同時給你編號跟對應邊烙的職
        if new < num:
            is_insert = True
            answer = answer[:index]+[new] + answer[index:]
            break
        else:
            answer = answer + [new]
else:
    answer = [new]
print(answer)

answer = [30, 40, 50, 60]
new = 20
if answer:
    is_insert = False
    for index, num in enumerate(answer):  # enumerate 同時給你編號跟對應邊烙的職
        if new < num:
            is_insert = True
            answer = answer[:index]+[new] + answer[index:]
            break
        else:
            answer = answer + [new]
else:
    answer = [new]
print(answer)
