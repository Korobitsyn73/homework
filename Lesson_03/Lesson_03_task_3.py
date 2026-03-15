from address import Address
from mailing import Mailing

to_address = Address('127000', 'Москва', 'Академика Королёва', '12', '45')
from_address = Address('450083', 'Уфа', 'Рихарда Зорге', '49', '261')
cost = 870
track = ('640370457')


my_mailing = Mailing(to_address, from_address, cost, track)

print(f'Отправление: {track} из {from_address} \
в {to_address}. Стоимость {cost} рублей.')
