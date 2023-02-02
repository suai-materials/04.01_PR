from datetime import date
from dataclass_csv import DataclassReader, dateformat, accept_whitespaces, DataclassWriter
from dataclasses import dataclass, field
from typing import List

@dateformat(' %Y-%m-%d')
@accept_whitespaces
@dataclass
class Client:
    last_name: str
    first_name: str
    second_name: str
    gender: str
    phone: str
    photo: str
    date_birthday: date
    Email: str
    date_reg: date


formatted_clients: List[Client] = []

if __name__ == '__main__':
    with open("stable_client_import.csv", "r", encoding="windows-1251", newline='') as f:
        dt = DataclassReader(f, Client, dialect='excel')
        dt.map("Фамилия").to("last_name")
        dt.map("Имя").to("first_name")
        dt.map("Отчество").to("second_name")
        dt.map("Пол").to("gender")
        dt.map("Телефон").to("phone")
        dt.map("Фотография клиента").to("photo")
        dt.map("Дата рождения").to("date_birthday")
        dt.map("Дата регистрации").to("date_reg")
        for client in dt:
            client.first_name = client.first_name.lstrip()
            client.second_name = client.second_name.lstrip()
            if len(client.first_name) == 0:
                (client.last_name, client.first_name, client.second_name) = client.last_name.split()
            client.gender = client.gender.lstrip().lower()
            if len(client.gender) > 1:
                client.gender = client.gender[0]
            client.phone = client.phone.lstrip()[:-1]
            client.Email = client.Email.lstrip()
            formatted_clients.append(client)

    with open("formatted_client_import.csv", "w", encoding="utf-8", newline='') as fw:
        DataclassWriter(fw, formatted_clients, Client).write()