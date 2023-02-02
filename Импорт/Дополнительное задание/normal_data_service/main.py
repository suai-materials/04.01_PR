import csv
import re
from dataclasses import dataclass
from typing import List
from dataclass_csv import DataclassWriter


@dataclass
class Service:
    name: str
    duration: int
    price: int
    discount: float


services: List[Service] = []

with open("service_a_import.txt", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f, dialect=csv.excel)
    # пропускаем заголовки
    reader.__next__()
    for el in reader:
        new_el = list(map(lambda l: l.lstrip(), el))
        (num, unit) = int(re.findall(r"\d+", new_el[1])[0]), re.findall(r"[а-я]+\.", new_el[1])[0]
        duration: int
        match unit:
            case "мин.":
                duration = num * 60
            case "час.":
                duration = num * 3600
            case _:
                duration = num
        price = int(re.findall(r"\d+", new_el[2])[0])
        try:
            discount = float("0." + re.findall(r"\d+", new_el[3])[0])
        except IndexError:
            discount = 0.
        services.append(Service(new_el[0], duration, price, discount))

with open("result.csv", "w", encoding="utf-8", newline="") as f:
    DataclassWriter(f, services, Service).write()
