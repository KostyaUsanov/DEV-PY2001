# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Car:
    """Класс описывает Машину"""

    def __init__(self, model_car: str, price: (int, float), type_car: str) -> None:
        """ Инициализация экземпляра класса.
        :param model_car: Марка машины
        :param price: цена
        :param type_car: тип машины

        Примеры:
        >>> car1 = Car('BMW', 5000000, 'Легковой')  # инициализация экземпляра класса
        >>> car2 = Car("Audi", 7000000, "Легковой") # инициализация экземпляра класса
        >>> car3 = Car("Mercedes", 20000000, "Грузовой")    # инициализация экземпляра класса
        """


        if not isinstance(model_car, str):
            raise TypeError("Марка машины должна быть типа str")  # вызываем ошибку
        self.model_car = model_car
        if not isinstance(price, (int, float)):
            raise TypeError("Цена машины должна быть типа int или float")  # вызываем ошибку
        self.price = price
        if not isinstance(type_car, str):
            raise TypeError("Тип машины должен быть типа str")  # вызываем ошибку
        self.type_car = type_car





    def is_truck_car(self)-> bool:
        """Функция которая проверяет является ли машина грузовой

        :return: Является ли машина грузовой

        Примеры:
        >>> car1 = Car('BMW', 5000000, 'Легковой')
        >>> car1.is_truck_car()
        >>> car2 = Car("Audi", 7000000, "Легковой")
        >>> car2.is_truck_car()
        >>> car3 = Car("Mercedes", 20000000, "Грузовой")
        >>> car3.is_truck_car()

        """
        ...

    def discount_from_price(self, discount: (int, float))-> None:
        """Функция которая дает скидку если цена больше 5999999

        :param discount: размер скидки

        :return: цена со скидкой

        Примеры:
        >>> car1 = Car('BMW', 5000000, 'Легковой')
        >>> car1.discount_from_price(0)
        >>> car2 = Car("Audi", 7000000, "Легковой")
        >>> car2.discount_from_price(10)
        >>> car3 = Car("Mercedes", 20000000, "Грузовой")
        >>> car3.discount_from_price(10)

        """
        ...

class Model_car:
    """Класс описывает Марку Машину"""

    def __init__(self, model: str, color: str, power: (int, float)) -> None:
        """ Инициализация экземпляра класса.

        :param model: Модель марки машины
        :param color: цвет марки машины
        :param power: мощность марки машины

        :raise TypeError: TypeError

        Примеры:
        >>> BMW1 = Model_car('X2', "Черный", 200)  # инициализация экземпляра класса
        >>> BMW2 = Model_car("X5", 'Белый', 250) # инициализация экземпляра класса
        >>> BMW3 = Model_car("X6", 'Красный', 300)    # инициализация экземпляра класса
        """


        if not isinstance(model, str):
            raise TypeError("Модель Марки машины должна быть типа str")  # вызываем ошибку
        self.model = model
        if not isinstance(color, str):
            raise TypeError("Цвет машины должна быть типа str")  # вызываем ошибку
        self.color = color
        if not isinstance(power, str):
            raise TypeError("Мощность машины должна быть типа int или float")  # вызываем ошибку
        self.power = power



    def change_color(self, color: str) -> None:
        """
        Функция, которая меняет цвет марки машины на белый если она другого цвета
    
        param color: Белый цвет

        Примеры:
        >>> BMW1 = Model_car('X2', 'Черный', 200)  # инициализация экземпляра класса
        >>> BMW1.change_color('Белый')
        >>> BMW2 = Model_car("X5", 'Белый', 250) # инициализация экземпляра класса
        >>> BMW2.change_color('Белый')
        >>> BMW3 = Model_car("X6", "Красный", 300)    # инициализация экземпляра класса
        >>> BMW3.change_color('Белый')
        """
        ...
    def max_power(self):
        """
        Функция, которая проверяет максимальную мощность авто

        Примеры:
        >>> BMW1 = Model_car('X2', 'Черный', 200)  # инициализация экземпляра класса
        >>> BMW1.max_power()
        >>> BMW2 = Model_car("X5", 'Белый', 250) # инициализация экземпляра класса
        >>> BMW2.max_power()
        >>> BMW3 = Model_car("X6", "Красный", 300)    # инициализация экземпляра класса
        >>> BMW3.max_power()
        """

        ...


class WeightAuto:
    """Класс описывает Вес Авто"""

    def __init__(self):
        """ Инициализация экземпляра класса.

        :param max_weight: Максимальный вес загрузки авто
        :param weight: вес незагруженного авто
        """
        self.max_weight = 10000
        self.weight = 3000

    def increment_add_to_weight(self, add_to_weight: (int, float)):
        """
        Метод увеличивает вес последней загрузки машины.

       :param add_to_weight: Количество добавленного груза
        """
        if not isinstance(add_to_weight, int):  # проверяем, что добавление груза к весу типа int или float
            raise TypeError("Добавление груза должны быть типа int или float")  # вызываем ошибку

        if add_to_weight > self.max_weight:
            raise ValueError("Добавление груза не должно быть больше максимальной грузоподъемности")
        self.weight += add_to_weight

    def increment_del_to_weight(self, del_to_weight: (int, float)):
        """
        Метод уменьшает вес последней разгрузки машины.

        :param del_to_weight: Количество удаленного груза
        """
        if not isinstance(del_to_weight, (int, float)):  # проверяем, что удаление груза к весу типа int или float
            raise TypeError("УКоличество удаленного груза должны быть типа int или float")  # вызываем ошибку

        if del_to_weight > self.weight:
            raise ValueError("Количество удаленного груза не должно быть больше веса незагруженного авто")
        self.max_weight -= del_to_weight


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest

    doctest.testmod()
