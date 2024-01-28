class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self._day = day
        self._month = month
        self._year = year

        self.is_valid_date(self._day, self._month, self._year)

    @staticmethod       # TODO какой декоратор следует применить?
    def is_leap_year(year: int) -> bool:
        """Проверяет, является ли год високосным"""

        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return True
        else:
            return False  # TODO записать условие проверки високосного года

    @staticmethod
    def get_max_day(month: int, year: int) -> int:
        """Возвращает максимальное количество дней в месяце для указанного года"""
        if Date.is_leap_year(year):
            data = Date.DAY_OF_MONTH[1]
            return data[month]
        else:
            return Date.DAY_OF_MONTH[0][month]  # TODO вернуть количество дней указанного месяца

    @staticmethod
    def is_valid_date(day: int, month: int, year: int) -> None:
        if day > Date.get_max_day(month, year):
            raise ValueError     # TODO если указанный набор день, месяц и год неверны, то вызвать ошибку ValueError

    @property
    def day(self) -> int:
        return self._day

    @day.setter
    def day(self, day: int) -> None:
        if 0 <= day <= 31:
            raise ValueError('ValueError')
        if not isinstance(day, int):
            raise TypeError('TypeError')
        self._day = day       # TODO записать getter и setter для дня

    @property
    def month(self) -> int:
        return self._month

    @month.setter
    def month(self, month: int) -> None:
        if not isinstance(month, int):
            raise TypeError('TypeError')
        if 0 <= month < 12:
            raise ValueError('ValueError')
        self._month = month  # TODO записать getter и setter для месяца

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, year: int) -> None:
        if not isinstance(year, int):
            raise TypeError('TypeError')
        if year <= 0:
            raise ValueError('ValueError')
        self._year = year  # TODO записать getter и setter для года


Date.is_valid_date(11, 1, 2000)


