from Time import Time
from WorkDay import WorkDay
from Scooter import Scooter

print('Input time (second, minute, hour): ')
time1 = Time(input(), input(), input())
print(time1)
print('\nCount of seconds: ')
print(time1.countSecond())
time1.plusFiveSecond()
print('\n+5 second: ')
print(time1)
print('\nCount of seconds: ')
print(time1.countSecond())

workDay1 = WorkDay(_surname='Morozov', _paymentHour=200)
workDay1.hour = 10
workDay1.CalculateSalary()
print('\n', workDay1, '\n')

scooter1 = Scooter()
print(scooter1)
scooter2 = Scooter(_uniqueId=117, _paymentSecond=2)
scooter2.minute = 10
scooter2.second = 10
print("\n Scooter 2:")
print(scooter2)
scooter2.Calculate()
print("\nafter calculating: ", scooter2)
scooter2.plusFiveSecond()
scooter2.Calculate()
print("\nafter calculating +5 seconds: ", scooter2)
