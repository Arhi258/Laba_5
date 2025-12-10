#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    # Список рейсов
    flights = []

    while True:
        command = input(">>> ").lower()

        # Команда завершения
        if command == 'exit':
            break

        # Команда добавления рейса
        elif command == 'add':
            destination = input("Пункт назначения: ").lower()
            number = int(input("Номер рейса: "))
            aircraft_type = input("Тип самолета: ").lower()

            flight = {
                'destination': destination,
                'number': number,
                'aircraft_type': aircraft_type
            }

            # Добавить словарь в список
            flights.append(flight)
            # Сортировка списка
            if len(flights) > 1:
                flights.sort(key=lambda item: item.get('destination', ''))

        # Вывод всех рейсов
        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+'.format(
                '-' * 30,
                '-' * 15,
                '-' * 20
            )
            print(line)
            print(
                '| {:^30} | {:^15} | {:^20} |'.format(
                    "Пункт назначения",
                    "Номер рейса",
                    "Тип самолета"
                )
            )
            print(line)

            for flight in flights:
                print(
                    '| {:>30} | {:>15} | {:>20} |'.format(
                        flight.get('destination', ''),
                        flight.get('number', ''),
                        flight.get('aircraft_type', '')
                    )
                )

            print(line)

        # Вывод рейсов с данным типом самолета
        elif command == 'check_flight':
            key_aircraft = input("Введите тип самолета: ")
            count = 0

            # Проверка, есть ли такой тип самолета
            for flight in flights:
                if flight.get("aircraft_type") == key_aircraft:
                    count += 1
                    print(
                        f"Вам подходит рейс {flight.get('number', '')}"
                        f" который направляется в "
                        f"{flight.get('destination', '')}"
                    )

            # Проверка, если нет такого типа самолета
            if count == 0:
                print(
                    "Похоже, рейсов с данным типом самолета нет,"
                    " но вы можете посмотреть другие рейсы"
                )

        # Справка о работе с программой
        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить рейс")
            print("list - вывести список рейсов")
            print("exit - завершить работу с программой")
            print("help - вывести список команд")
            print(
                "check_flight - проверить, "
                "есть ли рейс с данным типом самолета"
            )

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
