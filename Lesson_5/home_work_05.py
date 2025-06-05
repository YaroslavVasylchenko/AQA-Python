small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list

# small_list = set(small_list)
# print(small_list)

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
# small_list_count = sum(small_list)
# small_list_count1 = len(small_list)
# small_list_count2 = small_list_count / small_list_count1
# print(f"awr",(small_list_count2))

# task 3. Перевірте, чи є в списку big_list дублікати

# if len(big_list) != len(set(big_list)):
#     print ("have duble")
# else:
#     print("There are no duplicates")



base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
# key_1 = max(add_dict, key=add_dict.get)
# print("The key with the maximum value:", key_1)


# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику

# new_dict = {}
# for key, value in base_dict.items():
#     new_dict[value] = key
# print(new_dict)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх

# sum_dict = {}
# for key, value in base_dict.items():
#     sum_dict[key] = value
# for key, value in add_dict.items():
#     if key in sum_dict:
#         sum_dict[key] = str(sum_dict[key]) + str(value)
#     else:
#         sum_dict[key] = value

# print(sum_dict)



# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"
line2 = set(line)
print(line2)


# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
union_set = set_1^set_2
union_set = sum(union_set)
print(union_set)


# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]

list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]
set_1 =  set(list_1)
set_2 =  set(list_2)
set_3 = set_1 ^ set_2
print (set_3)

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]

age_groups = {}
for name, age in person_list:
    lower = (age // 10) * 10
    upper = lower + 9
    key = f'{lower}-{upper}'
    if key not in age_groups:
        age_groups[key] = []
    age_groups[key].append(name)

print(age_groups)

# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}