from Time import Time

class WorkDay(Time):
    __salary = 0

    def __init__(self, _surname = "None", _paymentHour = 0):
        self.__surname = _surname
        self.__paymentHour = _paymentHour
        Time.__init__(self)

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, newSurname):
        self.__surname = newSurname

    @property
    def paymentHour(self):
        return self.__paymentHour

    @paymentHour.setter
    def paymentHour(self, newPaymentHour):
        self.__paymentHour = newPaymentHour

    #Set a salary for one day
    def CalculateSalary(self):
        self.__salary = self.__paymentHour * self.hour

    def __str__(self):
        return "Surname: {}\n" \
                "Hour of work: {}\n" \
                "Salary for one day: {}" \
                .format(self.__surname, self.hour, self.__salary)
        