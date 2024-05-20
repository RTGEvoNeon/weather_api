import datetime
from typing import List

order_json = {
    'item_id': '123',
    'created_date': '2002-11-24 14:00',
    'pages_visited': [1, 3, 4],
    'price': 15.22
}

class Order:
    def __init__(self, item_id: int, created_date: datetime.datetime, pages_visited: List[int], price: float):
        self.pages_visited = pages_visited
        self.created_date = created_date
        self.price = price
        self.item_id = item_id

    def __str__(self):
        return str(self.__dict__)

a = Order(**order_json)
print(a)

