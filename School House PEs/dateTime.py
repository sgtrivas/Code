import datetime as d

today = d.datetime.today()
#year = datetime.datetime.now()
#print(f"the date is {year} ")
print("YEAR: "+ today.strftime("%Y"))
print("MONTH: "+ today.strftime("%m"))
print("DAY: " + today.strftime("%d"))

#using strftime("%Y-%m-%d %HH:%MM:%SS")
# print("YEAR: " + year.strftime("%Y"))
# print("MONTH: " + year.strftime("%m"))
# print("DAY: " + year.strftime("%d"))


date = input("Enter YYYY-MM-DD: ").split('-')
nyear = date[0]
nmonth = date[1]
nday = date[2]

print(f"Year: {nyear} \nMonth: {nmonth} \nDay: {nday}")