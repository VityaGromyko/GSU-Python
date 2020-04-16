# -*- coding: utf-8 -*-
"""
Задание 17.2

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
"""


# %%
import re
from pprint import pprint


def parse_sh_cdp_neighbors(command_output: str):
    name = re.search(r"(R|SW)\d", command_output)[0]
    find = re.findall(r"((?:R|SW)\d)\s+(Eth \d/\d)[\S\d ]+(Eth \d/\d)", command_output)
    output = {name: {}}
    for f in find:
        output[name][f[1]] ={f[0]: f[2]}
    return output


filenames = [f"sh_cdp_n_r{i}.txt" for i in range(1, 7)] + ["sh_cdp_n_sw1.txt"]
print(filenames)

# with open(filenames[-1]) as file:
#     pprint(parse_sh_cdp_neighbors(file.read()))

for filename in filenames:
    with open(filename) as file:
        pprint(parse_sh_cdp_neighbors(file.read()))
