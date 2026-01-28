from user import User


class User:

    my_user = User('Максим', 'Коробицын')
    print(my_user.first_name)
    print(my_user.last_name)
    print(my_user.namefam())
