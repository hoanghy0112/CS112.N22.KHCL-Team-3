from src.findNextDate import isValidDate, findNextDate

if __name__ == "__main__":
    day = int(input("Nhập ngày: "))
    month = int(input("Nhập tháng: "))
    year = int(input("Nhập năm: "))

    if not isValidDate(day, month, year):
        print("Ngày không hợp lệ")
    else:
        newDay, newMonth, newYear = findNextDate(day, month, year)
        print(
            f"Ngày tiếp theo của ngày {day}/{month}/{year} là {newDay}/{newMonth}/{newYear}"
        )
