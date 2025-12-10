#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = set(input("Введите первую строку: ").replace(" ", ""))
    b = set(input("Введите вторую строку: ").replace(" ", ""))

    common = a & b
    print(f"Общие символы: {common}")