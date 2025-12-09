#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Перевод всей строки в нижний регистр
    a = list(input("Введите строку: ").lower())
    vowels = {'у', 'е', 'ё', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю'}

    common = set(a) & vowels

    count = 0
    for i in common:
        count += a.count(i)

    print(f"Количество гласных в вашей строке = {count}")