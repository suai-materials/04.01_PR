from dataclasses import dataclass
from dataclass_csv import DataclassWriter
import csv
from typing import List
import os

import re


@dataclass
class User:
    login: str
    password: str
    role: str
    fio: str = ""
    photo: str = ""


DIRECTORY_NAME = "Фото пользователей"

users: List[User] = []
photos: List[str] = list(filter(lambda f: re.match(r'.*\.(gif|png|jpg)', f), os.listdir(DIRECTORY_NAME)))

if __name__ == '__main__':
    with open("Пользователи.csv", 'r', encoding='utf-8', newline="") as user_f:
        csvr = csv.reader(user_f, dialect=csv.excel)
        # Пропускаем первую строчку
        csvr.__next__()
        for el in csvr:
            users.append(User(el[2], el[3], el[4], "".join(el[:2])))
            try:
                # Можно оптимизировать скрипт и проходить по фото и искать к ним пользователей, но тут вопрос,
                # что у нас больше фото или пользователей
                users[-1].photo = os.path.abspath(
                    DIRECTORY_NAME + "\\" + list(filter(lambda f: re.match(rf'{el[2]}\..*', f), photos))[0])
            except IndexError:
                pass

    with open("new_users.csv", "w", encoding='utf-8', newline="") as user_w:
        DataclassWriter(user_w, users, User).write()
