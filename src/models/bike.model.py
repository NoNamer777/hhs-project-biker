from datetime import datetime


class Bike:
    __id = 'bike-0001'
    __is_electric = False
    __is_damaged = False
    __is_insured = False
    __cost = 200
    __gender = 'male'
    __rented_to = None
    __renting_period_start = None
    __renting_period_end = None
    __return_date = None

    def __init__(
        self,
        id: str,
        gender: str,
        is_electric: bool,
        is_damaged: bool,
        rented_to: object,
        cost: int,
        is_insured: bool,
        renting_period_start: datetime,
        renting_period_end: datetime,
    ):
        self.__id = id
        self.__gender = gender
        self.__is_electric = is_electric
        self.__is_damaged = is_damaged
        self.__rented_to = rented_to
        self.__cost = cost
        self.__is_insured = is_insured
        self.__renting_period_start = renting_period_start
        self.__renting_period_end = renting_period_end

    def __lt__(self, other):
        return self.id == other.id

    def is_rented_to(self, customer):
        return self.__rented_to is customer

    def is_damaged(self):
        return self.__is_damaged

    def is_electric(self):
        return self.__is_electric

    def is_for_gender(self, gender):
        return self.__gender is gender

    def is_insured(self):
        return self.__is_insured

    def return_bike(self):
        self.__return_date = datetime.now()

    def is_retrurned_on_time(self):
        return self.__renting_period_end >= self.__return_date
