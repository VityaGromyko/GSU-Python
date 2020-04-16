# -*- coding: utf-8 -*-
"""
Задание 17.2a

Создать функцию generate_topology_from_cdp, которая обрабатывает вывод команды show cdp neighbor из нескольких файлов и
записывает итоговую топологию в один словарь.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_filename - имя файла в формате YAML, в который сохранится топология.
 * значение по умолчанию - None. По умолчанию, топология не сохраняется в файл
 * топология сохраняется только, если save_to_filename как аргумент указано имя файла

Функция должна возвращать словарь, который описывает соединения между устройствами, независимо от того сохраняется ли
топология в файл.

Структура словаря должна быть такой:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}},
 'R5': {'Fa 0/1': {'R4': 'Fa 0/1'}},
 'R6': {'Fa 0/0': {'R4': 'Fa 0/2'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.

Проверить работу функции generate_topology_from_cdp на списке файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Проверить работу параметра save_to_filename и записать итоговый словарь в файл topology.yaml.
"""
# %%
import re
import yaml


def parse_sh_cdp_neighbors(command_output: str):
    name = re.search(r"(R|SW)\d", command_output)[0]
    find = re.findall(r"((?:R|SW)\d)\s+(Eth \d/\d)[\S\d ]+(Eth \d/\d)", command_output)
    output = {name: {}}
    for f in find:
        output[name][f[1]] = {f[0]: f[2]}
    return output


def generate_topology_from_cdp(list_of_files: list, save_to_filename: str = None):
    output = {}
    for filename in list_of_files:
        with open(filename) as file:
            output.update(parse_sh_cdp_neighbors(file.read()))
    if save_to_filename is not None:
        with open(save_to_filename, "w") as file:
            yaml.dump(output, file)
    return output


files = [f"sh_cdp_n_r{i}.txt" for i in range(1, 7)] + ["sh_cdp_n_sw1.txt"]
generate_topology_from_cdp(files, "Task2_output.yaml")
