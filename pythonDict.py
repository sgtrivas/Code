tickers = {'UA':'Under Armour','AMZN':'Amazon','SAP': 'SAP AG'}
positions = {1:"First", 2:"Second",3:"Third"}
empty = {}


#get specific values from the dictionary
print('tickers[SAP]:',tickers.get('AMZN'))
print('tickers.get(AMZN):',tickers.get('AMZN'))
print('tickers.get(MSFT):',tickers.get('MSFT'))
print('tickers.get(MSFT, Key not found):', tickers.get('MSFT', 'Key not found'))
print('-' * 70)


#add new key value pairs
tickers['FIT'] = 'Fitbit, Inc.'
tickers['APPL'] = 'Apple, Inc.'
print(tickers)
print('-' * 70)


tickers['AMZN'] = 'Amazon.com, Inc.'
print(tickers)
print('-' * 70)

