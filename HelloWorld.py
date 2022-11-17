year = int(input("Please enter a year: "))
divided_by_4 = year%4 == 0
not_divided_by_100 = year%100!=0
divided_by_400 = year%400==0
lap_year = divided_by_400  or (divided_by_4 and not_divided_by_100)

print ("is the ", year, " a lap year? ", lap_year)