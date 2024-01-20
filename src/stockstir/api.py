import requests

# Thank you for suggesting API support! (still in early stages)
class API:
	def __init__(self):
		pass
	# API class that allows for the gathering of data from the internet through APIs.
	
	# Initial implementation of the Alpha Vantage API:
	def get_alpha_vantage_data(self, stock_symbol, api_key, type='TIME_SERIES_INTRADAY'):
		# Get the URL for the API:
		url = 'https://www.alphavantage.co/query?function=' + type + '&symbol=' + stock_symbol + '&interval=5min&apikey=' + api_key
		r = requests.get(url)
		data = r.json()
		return data
	
	# For the CNBC 'API' json structure. This is not an actual API, but rather a JSON structure that is used to get various information on a company stock.
	# Thank you Gr1pp717 (https://www.reddit.com/user/Gr1pp717/) for the research and resources used in the methods below!
	def get_cnbc_api_json_data(self, stock_symbol):
		cnbc_api_url = 'https://quote.cnbc.com/quote-html-webservice/restQuote/symbolType/symbol?symbols=' + stock_symbol
		r = requests.get(cnbc_api_url)
		data = r.json()
		return data
	
	def list_cnbc_data(self, stock_symbol):
		data = self.get_cnbc_api_json_data(stock_symbol)
		formatted_dictionary_data = data['FormattedQuoteResult']['FormattedQuote'][0]
		keys = list(formatted_dictionary_data.keys())
		values = list(formatted_dictionary_data.values())
		for i in range(len(keys)):
			print(f"Index Value: {i}. {keys[i]}: {values[keys.index(keys[i])]}")
		return keys, values
	
	# Get a single price using the CNBC 'API'
	def get_price_cnbc_api(self, stock_symbol):
		data = self.get_cnbc_api_json_data(stock_symbol)
		price = data['FormattedQuoteResult']['FormattedQuote'][0]['last']
		return price