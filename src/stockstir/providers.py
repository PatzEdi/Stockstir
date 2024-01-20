from urllib.request import Request, urlopen


class Providers:
	# These two functions are solely used for the __init__.py file.
	def __init__(self, provider_name="cnbc"):
		if provider_name == "cnbc":
			self.provider_number = 0
		elif provider_name == "cnn":
			self.provider_number = 1
		elif provider_name == "zacks":
			self.provider_number = 2
		else:
			print("Invalid provider name. Using default provider (cnbc)")
			self.provider_number = 0

	def set_gather_info(self, gather_info):
		self.gather_info = gather_info

	providers = {
		"https://www.cnbc.com/quotes/": '(?<="price":")(.*)(?=","priceChange":")',
		"https://money.cnn.com/quote/quote.html?symb=": 'BatsUS">(.*?)</span>',
		"https://www.zacks.com/stock/quote/": 'last_price">\$(.*?)<span>',
	}

	provider_number = 0
	# This is the main function to check and see if each provider is working, and if not, it will print out a message saying which provider is not working.
	def run_provider_checks(self, test_ticker_symbol="AMZN", exit_on_failure=True):
		temp_provider_number = self.provider_number
		is_passing = True
		dictionary_size = len(self.providers)
		print(f"Running REQUEST and REGEX source checks with '{test_ticker_symbol}' symbol\n")
		for i in range(dictionary_size):
			test_url = list(self.providers.keys())[i] + str(test_ticker_symbol)
			self.provider_number = i
			print("TESTING SOURCE NUMBER " + str(i) + "... (" + test_url + ")")
			try:
				req = Request(
					url=list(self.providers.keys())[self.provider_number] + str(test_ticker_symbol),
					headers={'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0"}
				)
				source = str(urlopen(req).read())
				print("REQUEST check for Source number " + str(i) + " is working.")
				try:
					self.gather_info.gather_price(source)
					print(f"REGEX check for Source number {i} is working.\n")
				except:
					print(f"REGEX check for Source number {i} is NOT working.\n")
					is_passing = False
			except:
				print(f"REQUEST check for Source number {i} is NOT working.\n")
				is_passing = False
		if is_passing:
			print("All providers are working.\n")
		else:
			print("\nSome providers are not working. Verify that the ticker symbol is valid, or create an issue if persistent.\n")
			if exit_on_failure:
				print("\nexit_on_failure is set to True. Exiting...")
				exit()
		self.provider_number = temp_provider_number
		return is_passing
	# This function is used to test a specific provider, and if it fails, it will return False, and if it passes, it will return True.
	def test_selected_provider(self, test_ticker_symbol="AMZN"):
		is_passing = True
		try:
			req = Request(
				url=list(self.providers.keys())[self.provider_number] + str(test_ticker_symbol),
				headers={'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0"}
			)
			source = str(urlopen(req).read())
		except:
			is_passing = False
		try:
			self.gather_info.gather_price(source)
		except:
			is_passing = False
		return is_passing