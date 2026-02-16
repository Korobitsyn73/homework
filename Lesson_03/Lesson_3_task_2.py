from smartphone import Smartphone


my_phone = [
    Smartphone('Xiaomy', 'Redmi Note 13', '+79174097857'),
    Smartphone('Samsung', 'Galaxy S25', '+79188747094'),
    Smartphone('iPhone', '17', '+79269473620'),
    Smartphone('Honor', '200 Pro', '+79876396483'),
    Smartphone('Xiaomy', 'Poco', '+79270908796')]


for smartphone in my_phone:
    print(f'{smartphone.brand}, {smartphone.model}, {smartphone.number}')
