def is_year_leap(year):
    if year < 1582:
        return False
    elif year % 4 !=0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
    
        
def days_in_month(year, month):
    monthDays = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_year_leap(year):
        if month == 2:
            return 29
    return monthDays[month-1]
    
    
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

