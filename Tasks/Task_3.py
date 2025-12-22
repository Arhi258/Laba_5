#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    school = {}

    while True:
        command = input(">>> ").lower()

        # Выход из программы
        if command == "exit":
            break

        # Добавление класса
        elif command == "add":
            class_school = input("Введите номер класса и его букву: ").lower()
            number_of_students = int(input(
                "Введите количество учеников в классе: "
            ))

            school[class_school] = number_of_students

        # Удаление класса
        elif command == "remove":
            class_remove = input(
                "Введите класс (и его букву), который был расформирован: "
            ).lower()

            if class_remove not in school:
                print("Такого класса нет!")
            else:
                del school[class_remove]

        # Вывод суммы учеников в школе
        elif command == "sum":
            all_students = sum(school.values())
            print(f"Всего учащихся в школе: {all_students}")

        # Изменение количества учеников
        elif command == "change":
            class_change = input(
                "Введите класс (и его букву), который был изменен: "
            )

            if class_change not in school:
                print("Такого класса нет!")
            else:
                school[class_change] = int(input(
                    "Введите новое число учеников в классе: "
                ))

        # Вывод всех классов в школе
        elif command == "list":
            # Заголовок таблицы
            line = '+--------+------------------+'
            print(line)
            print(
                '| {:^6} | {:^16} |'.format(
                    'Класс',
                    'Кол-во учеников'
                )
            )
            print(line)

            # Вывод данных о классах и количестве учеников
            for class_school, number_of_students in school.items():
                print(
                    '| {:>6} | {:>16} |'.format(
                        class_school,
                        number_of_students
                    )
                )
                print(line)

        # Вывод списка команд
        elif command == "help":
            print("list - вывод всех классов в школе")
            print("help - вывод списка команд")
            print("change - изменение количества учениклв в классе")
            print("sum - вывод общего количества учеников в школе")
            print("remove - удаление класса")
            print("add - добавление нового класса")
            print("exit - завершение работы программы")

        # Действие при неверной команде
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


