MAX_SECOND = 60
MAX_MINUTE = 60
MAX_HOUR = 24


class Time:

    def __init__(self, second = None, minute = None, hour = None):
        check = True
        try:
            second = int(second)
            minute = int(minute)
            hour = int(hour)
        except (ValueError, TypeError):
            check = False

        if check and\
            0 <= second < MAX_SECOND and\
            0 <= minute < MAX_MINUTE and\
            0 <= hour < MAX_HOUR:
            self.__second = second
            self.__minute = minute
            self.__hour = hour
            print('Object created with certain value')
        else:
            self.__second = 0
            self.__minute = 0
            self.__hour = 0
            print("Value error: default value was set")


    def __del__(self):
        print("Object was deleted")

    @property
    def second(self):
       return self.__second

    @second.setter
    def second(self, newSecond):
        if newSecond in range(0, MAX_SECOND):
           self.__second = newSecond
        else:
          print("Unacceptable value")


    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, newMinute):
        if newMinute in range(0, MAX_MINUTE):
            self.__minute = newMinute
        else:
            print("Unacceptable value")

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, newHour):
        if newHour in range(0, MAX_HOUR):
            self.__hour = newHour
        else:
            print("Unacceptable value")

    def __str__(self):
        return "{}:{}:{}".format(self.__hour, self.__minute, self.__second)

    def countSecond(self):
        return self.__second + self.__minute * 60 + self.__hour * 60 * 24

    def plusFiveSecond(self):
        self.__second += 5
        if self.__second >= MAX_SECOND:
            self.__second -=60
            self.__minute += 1
            if self.__minute == MAX_MINUTE:
                self.__minute = 0
                self.__hour += 1
                if self.__hour == MAX_HOUR:
                    self.__hour = 0

