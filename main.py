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
scooter1 = Scooter(input(), input())
print(scooter1)
