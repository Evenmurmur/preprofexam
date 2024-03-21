"""Файл для решения задачи 3 предпроф экзамена.
Программа позволяет найти список вакансий по названию компании"""

with open("vacancy.csv", encoding="utf-8") as file:
    data = list(file)

for i in range(len(data)):
    data[i] = data[i].split(';')
    if i + 1 != len(data):
        data[i][-1] = data[i][-1][:-1]

name = input()

while name != "None":
    done = 0
    for i in data:

        if i[4] == name:
            print(f"{i[3]}")
            done += 1
            break

    if done == 0:
        print("К сожалению, ничего не удалось найти")
    name = input()
