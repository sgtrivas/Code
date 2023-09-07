import pyinputplus as pyip

birthDay = pyip.inputNum(prompt="enter the day you born (1 - 31): "+ "\n")
birthMonth = pyip.inputNum(prompt="enter the month you born (1 - 12): "+ "\n")


if birthDay >=22 and birthDay <=31 and birthMonth == 12 or birthDay >=1 and birthDay <= 19 and birthMonth == 1: 
    print("You are a Capricorn\n" + " \U00002651"*5)
elif birthDay >=20 and birthDay <=30 and birthMonth == 1 or birthDay >=1 and birthDay <= 18 and birthMonth == 2:
    print("You are a Aquarius\n" + " \U00002652"*5)
elif birthDay >=19 and birthDay <=29 and birthMonth == 2 or birthDay >=1 and birthDay <= 20 and birthMonth == 3:
    print("You are a Pisces\n" + " \U00002653"*5)
elif birthDay >=21 and birthDay <=31 and birthMonth == 3 or birthDay >=1 and birthDay <= 19 and birthMonth == 4:
    print("You are a Aries\n" + " \U00002648"*5)
elif birthDay >=20 and birthDay <=30 and birthMonth == 4 or birthDay >=1 and birthDay <= 20 and birthMonth == 5:
    print("You are a Taurus\n" + " \U00002649"*5)
elif birthDay >=21 and birthDay <=31 and birthMonth == 5 or birthDay >=1 and birthDay <= 20 and birthMonth == 6:
    print("You are a Gemini\n" + " \U0000264A"*5)
elif birthDay >=21 and birthDay <=30 and birthMonth == 6 or birthDay >=1 and birthDay <= 22 and birthMonth == 7:
    print("You are a Cancer\n" + " \U0000264B")
elif birthDay >=23 and birthDay <=31 and birthMonth == 7 or birthDay >=1 and birthDay <= 22 and birthMonth == 8:
    print("You are a Leo\n" + " \U0000264C"*5)
elif birthDay >=23 and birthDay <=31 and birthMonth == 8 or birthDay >=1 and birthDay <= 22 and birthMonth == 9:
    print("You are a Virgo\n" + " \U0000264D"*5)
elif birthDay >=23 and birthDay <=30 and birthMonth == 9 or birthDay >=1 and birthDay <= 22 and birthMonth == 10:
    print("You are a Libra\n" + " \U0000264E"*5)
elif birthDay >=23 and birthDay <=31 and birthMonth == 10 or birthDay >=1 and birthDay <= 21 and birthMonth == 11:
    print("You are a Scorpio\n" + " \U0000264F"*5)
elif birthDay >=22 and birthDay <=30 and birthMonth == 11 or birthDay >=1 and birthDay <= 21 and birthMonth == 12:
    print("You are a Sagittarius\n" + " \U00002650"*5)

else:
    print("Invalid Birthdate")