from Time import Time

class Scooter(Time):
    __price = 0

    def __init__(self, _uniqueId = 0, _paymentSecond = 0):
        self.__uniqueId = _uniqueId
        self.__paymentSecond = _paymentSecond
        Time.__init__(self)

    @property
    def uniqueId(self):
        return self.__uniqueId

    @uniqueId.setter
    def uniqueId(self, newUniqueId):
        self.__uniqueId  = newUniqueId

    @property
    def paymentSecond(self):
        return self.__paymentSecond

    @paymentSecond.setter
    def paymentSecond(self, newPaymentSecond):
        self.__paymentSecond = newPaymentSecond

    #Set a price for scooter (all time)
    def Calculate(self):
        self.__price = self.__paymentSecond * Time.countSecond(self)

    def __str__(self):
        return "member id: {}\n"\
                "Price: {}\n"\
                .format(self.__uniqueId, self.__price)

