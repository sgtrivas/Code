import pyinputplus as pyip
tickers = {'UA': 'Under Armour', 'AMZN': 'Amazon', 'SAP': 'SAP AG', 'FIT': 'Fitbit, Inc.', 'APPL': 'Apple, Inc.'}

checkFor = pyip.inputStr(prompt="company do you want to check for in the list? ")

if checkFor in tickers or checkFor in tickers.values():
    print("Its here!")
else:
    print("it's not")