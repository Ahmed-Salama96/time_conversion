#!/bin/python3


def time_conversion(s):
    am_pm = s[-2:]
    hour = s[:2]
    time_24 = s[:-2]

    if am_pm == 'AM':
        if hour == '12':
            time_24 = '00' + time_24[2:]
    else:
        if int(hour) < 12:
            time_24 = str(12 + int(hour)) + time_24[2:]

    return time_24


if __name__ == '__main__':
    s = input()

    result = time_conversion(s)
    print(result)
