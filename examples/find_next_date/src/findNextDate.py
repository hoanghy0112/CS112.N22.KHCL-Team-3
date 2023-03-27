def isLeapYear(year: int) -> bool:
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def getMonthLength(month: int, year: int) -> int:
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month == 2:
        if isLeapYear(year):
            return 29
        else:
            return 28
    else:
        return 30


def isValidDate(day: int, month: int, year: int) -> bool:
    if month < 1 or month > 12:
        return False
    if day < 0 or day > getMonthLength(month, year):
        return False
    return True


def findNextDate(day: int, month: int, year: int) -> tuple:
    if not isValidDate(day, month, year):
        raise ValueError(f"{day}/{month}/{year} is not a valid date")

    if day < getMonthLength(month, year):
        day += 1
    else:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1

    return (day, month, year)


# if __name__ == "__main__":
#     year = int(input("Input a year: "))
#     month = int(input("Input a month [1-12]: "))
#     day = int(input("Input a day [1-31]: "))

#     if not isValidDate(day, month, year):
#         print("The date %d-%d-%d is invalid." % (day, month, year))
#     else:
#         print(
#             "The next date is [dd-mm-yyyy] %d-%d-%d." % findNextDate(day, month, year)
#         )
