import csv
import datetime
from dataclasses import dataclass
from dataclass_csv import DataclassWriter, dateformat
from typing import Dict, List


@dataclass
class ClientService:
    client_id: int
    start_time: datetime.datetime
    service_id: int


id_last_names: Dict[str, int] = {}
id_services: Dict[str, int] = {}
client_services: List[ClientService] = []

with open("client_from_db.csv", "r", encoding="utf-8", newline='') as f:
    reader = csv.reader(f, dialect=csv.excel)
    reader.__next__()
    id_last_names = dict(map(lambda row: (row[1], int(row[0])), reader))

with open("service_from_db.csv", "r", encoding="utf-8", newline='') as f:
    reader = csv.reader(f, dialect=csv.excel)
    reader.__next__()
    id_services = dict(map(lambda row: (row[1], int(row[0])), reader))

with open("clientservice_a_import.csv", "r", encoding="windows-1251", newline='') as f:
    reader = csv.reader(f, dialect=csv.excel)
    reader.__next__()
    client_services = list(
        map(lambda row: ClientService(id_last_names[row[0]], datetime.datetime.strptime(row[1], "%m/%d/%Y %H:%M"),
                                      id_services[row[2]]), reader))

with open("result.csv", "w", encoding="utf-8", newline='') as fw:
    DataclassWriter(fw, client_services, ClientService)
