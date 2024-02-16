import re
import random
from urllib.request import Request, urlopen


class GatherInfo:
	# Used for the __init__.py file.
	def set_providers(self, providers):
		self.providers = providers
	# This is the main function that uses a regex pattern to gather the price from the source.
	def gather_price(self, source):
		regex_pattern = list(self.providers.providers.values())[self.providers.provider_number]
		price = re.findall(regex_pattern, source)
		counter = 0
		for i in range(len(price)):
			try:
				float(price[i])
				break
			except:
				counter += 1
		price = float(price[counter].replace(",", ''))
		return price
	# Main function that gets the source from a provider (url) and returns it. This get_source function also contains the fail-safe mechanism within it, which changes provider in case one fails during the request, or if the regex does not work.
	def get_source(self, stock_symbol, random_user_agent=False, proxy=""):
		user_agents = [
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
			"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
			"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
			"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
			"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
			"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
			"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
			"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
			"Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
			"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
			"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0",
		]
		user_agent_pick = user_agents[len(user_agents) - 1]
		if random_user_agent:
			user_agent_pick = random.choice(user_agents)
		# This below is the fail-safe mechanism:
		failed_providers = []
		while True:
			try:
				req = Request(
					url=list(self.providers.providers.keys())[self.providers.provider_number] + str(stock_symbol),
					headers={'User-Agent': user_agent_pick}
				)
				source = str(urlopen(req).read())
				self.gather_price(source)
				return source
			except:
				if not self.providers.test_selected_provider():
					print(f"ERR: Provider {self.providers.provider_number} failed. Switching to a different provider...")
					failed_providers.append(self.providers.provider_number)
					while self.providers.provider_number in failed_providers:
						if len(failed_providers) != len(self.providers.providers):
							self.providers.provider_number = random.randint(0, len(self.providers.providers) - 1)
						else:
							raise Exception(
								f"\nAll providers seemed to have failed while trying to make a request. Please create an issue if persistent. Try to use get_price_cnbc_api('{stock_symbol}') found in the API class instead."
							)
				else:
					raise Exception(f"ERR: Could not find symbol/company through source {self.providers.provider_number}'s indexes.")
