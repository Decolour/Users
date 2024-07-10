class User():
    users = []

    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        User.users.append(self.__name)
        self.__access_level = 'user'
        print(f'Пользователь {self.__name} создан')

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_access_level(self):
        return self.__access_level


class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.__access_level = 'admin'

    def add_user(id, name, access_level='user'):
        if access_level == 'admin':
            new_user = Admin(id, name)
        elif access_level == 'user':
            new_user = User(id, name)
        else:
            raise ValueError("Неверно указан уровень доступа.")
        return new_user

    def delete_user(user):
        User.users.remove(user)

    def get_users():
        return User.users

    def get_user_info(user: User):
        if isinstance(user, User):
            return user.get_id(), user.get_name(), user.get_access_level()
        else:
            return print('Пользователь не найден')

    def rename_user(user, new_name):
        user.set_name(new_name)


Administrator = Admin(1, 'Administrator')
Petya = User(2, 'Петя')
Vasya = User(3, 'Вася')
Vitya = User(4, 'Витя')

print(Admin.get_users())
print(Admin.get_user_info(Vitya))
Admin.rename_user(Vitya, 'Витюня')
print(Admin.get_user_info(Vitya))
Sergey = Admin.add_user(8, 'Сергей', 'admin')
print(Admin.get_users())
Admin.delete_user('Administrator')
print(Admin.get_users())
