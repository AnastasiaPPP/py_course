import os
from pathlib import Path
from random import random, randint, choice
from exceprtions import FileNameException, ExtensionException


def rename_files(wanted_name: str, count_nums: int, old_extension: str, new_extension: str, range_: list):
    start_num = 1
    if not isinstance(wanted_name, str):
        raise FileNameException
    if old_extension[0] != '.' or new_extension[0] != '.':
        raise ExtensionException
    for obj in os.listdir():
        if obj[-len(old_extension):] == old_extension:
            new_name = f'{obj[range_[0]:range_[1] + 1]}{wanted_name}{start_num:0{count_nums}}{new_extension}'
            Path(obj).rename(new_name)
            start_num += 1


def add_two_numbers_to_file(line_count: int, filename: str):
    if not isinstance(filename, str):
        raise FileNameException
    if not isinstance(line_count, int):
        raise FileNameException
    with open(filename, 'a', encoding='utf-8') as file:
        for _ in range(line_count):
            file.write(f'{randint(-1000, 1000)} | {"{:.2f}".format(random()*1000)}\n')


def generate_names(count: int):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    with open('names.txt', 'a', encoding='utf-8') as file:
        for _ in range(count):
            name = ''
            for _ in range(randint(4, 7)):
                name += choice(letters)
            name = name.capitalize()
            file.write(f'{name}\n')


def name_sum(nums_file: str, names_file: str):
        with (
                open(nums_file, 'r', encoding="utf-8") as nums,
                open(names_file, 'r', encoding='utf-8') as names,
                open('new_file.txt', 'a', encoding='utf-8') as file
        ):
            nums_list = nums.readlines()
            names_list = names.readlines()
            for line1, line2 in zip(nums_list, names_list):
                res = int(line1[:line1.index('|') - 1]) * float(line1[line1.index('|') + 1:])
                if res < 0:
                    file.write(line2[:-2].upper() + "  ")
                    file.write(str(abs(res)) + "\n")
                else:
                    file.write(line2[:-2].lower() + "  ")
                    file.write('{:.0f}'.format(res) + "\n")

