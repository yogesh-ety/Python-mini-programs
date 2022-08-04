random_list = []

for i in range(101):
    random_list.append(i)

index = int(len(random_list) / 2)
mid = int(random_list[index])


print(random_list)

print(mid)

user_number = input("Enter the number to be searched between 0  to  100 :")

user_number = int(user_number)


def right_array(arr_1):
    global random_list
    for n in range(arr_1):
        random_list[n] = random_list[(arr_1 + 1) + n]
        random_list.remove(random_list[(arr_1 + 1) + n])


def left_array(arr_2):
    global random_list
    for m in range(arr_2):
        random_list.remove(random_list[(arr_2 + 1) + m])


while mid:
    if mid < user_number:
        right_array(mid)
        mid = mid / 2

    elif mid > user_number:
        left_array(mid)
        mid = mid / 2

    if mid == user_number:
        break

print("The number entered by the user is :")
print(mid)
