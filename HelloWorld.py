def is_it_lap_year(year):
    divided_by_4 = year % 4 == 0
    not_divided_by_100 = year % 100 != 0
    divided_by_400 = year % 400 == 0
    lap_year = divided_by_400 or (divided_by_4 and not_divided_by_100)
    if (lap_year):
        print("Year", year, "is a lap year")
    else:
        print("Year", year, "is not a lap year")
    return lap_year
    # print("is the", year, "a lap year? ", print ("Yes") if lap_year else print("No"))


if __name__ == '__main__':
    year = int(input("Please enter a year: "))
    is_it_lap_year(year)


def test_lap_year():
    assert is_it_lap_year(2020) == True


def test_not_lap_year():
    assert is_it_lap_year(2022) == False
