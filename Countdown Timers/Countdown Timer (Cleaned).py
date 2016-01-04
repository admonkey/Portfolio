#!/usr/local/bin/python3.5

import time, datetime
from subprocess import call

Year = 2017
Month = 12
Day = 30
Hour = 0
Minute = 0
Second = 0

while True:
	Datetime = datetime.datetime(Year, Month, Day, Hour, Minute, Second)
	diff = Datetime - datetime.datetime.now()
	diff = str(diff)

	day_str, not_useful, time_str = diff.split()
	hour_str, minute_str, second = time_str.split(":")
	second_str, not_useful = second.split(".")

	Day0 = day_str # Day
	Hour0 = hour_str # Hour
	Minute0 = minute_str # Min
	Second0 = second_str # Sec

	years = int(day_str) / float(365)

	year_final, year_fraction = divmod(years, 1)
	int_year_final = int(year_final)
	str_years_final = str(int_year_final)

	rounded_days = round(year_fraction * 365.25)
	int_days_final = int(rounded_days)
	str_days_final = str(int_days_final)

	Year1 = str_years_final + " " + "Year" # Year
	Day1 = str_days_final + " " + "Day" # Day
	Hour1 = Hour0 + " " + "Hour" # Hour
	Minute1 = Minute0 + " " + "Minute" # Min
	Second1 = Second0 + " " + "Second" # Sec

	Date0 = [Year1]
	Date1 = [Day1]
	Date2 = [Hour1]
	Date3 = [Minute1]
	Date4 = [Second1]


	for str0 in Date0:
		if (str0 != str(0) + " " + "Year"):
			if (str(str_years_final) == str(01)):
				print("-" * 10)
				print("|" + " " + str0 + " " + "|")
				print("-" * 10)
			else:
				print("-" * 13)
				print("|" + " " + str0 + "s" + " " + "|")
				print("-" * 13)

	for str1 in Date1:
		if (str1 != str(0) + " " + "Day"):
			if (str(Day0) == str(01)):
				print("-" * 9)
				print("|" + " " + str1 + " " + "|")
				print("-" * 9)
			else:
				print("-" * 12)
				print("|" + " " + str1 + "s" + " " + "|")
				print("-" * 12)

	for str2 in Date2:
		if (str2 != str(0) + " " + "Hour"):
			if (str(Hour0) == str(01)):
				print("----------")
				print("|" + " " + str2 + " " + "|")
				print("----------")
			else:
				print("-" * 12)
				print("|" + " " + str2 + "s" + " " + "|")
				print("-" * 12)

	for str3 in Date3:
		if (str3 != str(0) + " " + "Minute"):
			if (str(Minute0) == str(01)):
				print("----------")
				print("|" + " " + str3 + " " + "|")
				print("----------")
			else:
				print("-" * 14)
				print("|" + " " + str3 + "s" + " " + "|")
				print("-" * 14)

	for str4 in Date4:
		if (str4 != str(0) + " " + "Second"):
			if (str(Second0) == str("01")):
				print("-" * 13)
				print("|" + " " + str4 + " " + "|")
				print("-" * 13)
			else:
				print("-" * 14)
				print("|" + " " + str4 + "s" + " " + "|")
				print("-" * 14)
				
	time.sleep(1)