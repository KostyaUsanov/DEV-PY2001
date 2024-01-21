class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )
    a = [["1"], "afsfs"]
    a[0][0]
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)

    def is_leap_year(self, year: int):
        """Проверяет, является ли год високосным"""

        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return True
        else:
            return False




    @staticmethod
    def get_max_day(month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        if Date.is_leap_year(year):
            data = Date.DAY_OF_MONTH[1]
            return data[month]
        else:
            return Date.DAY_OF_MONTH[0][month]



                    # TODO используя атрибут класса DAY_OF_MONTH вернуть количество дней в запрашиваемом месяце и году
    @classmethod
    def is_valid_date(self, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""







      # TODO проверить валидность даты