#!/usr/bin/env python3

#Library used to gather information values of a company and its stock. 

import requests
import urllib
import urllib.request
from urllib.request import Request, urlopen
import re
import time
import random
#CREATED BY PATZEDI: https://github.com/PatzEdi , https://patzedi.github.io , https://twitter.com/patzedi

class Providers:
	# Here lets write a dictionary with the above source links as the key, and their respected regex as the value:
	# Dictionary:
	providers = {
		"https://www.cnbc.com/quotes/": '(?<="price":")(.*)(?=","priceChange":")',
		"https://money.cnn.com/quote/quote.html?symb=": 'BatsUS">(.*?)</span>',
		"https://www.zacks.com/stock/quote/": 'last_price">\$(.*?)<span>',
	}
	
	
	# This is the variable that will be used to determine which source to use in the dictionary above:
	provider_number = 0

	# Use user agents to run the tests, as certain websites/providers will block the requests if they are not from a browser:
	def runProviderChecks(testTickerSymbol = "AMZN", exitOnFailure = True):
		temp_provider_number = Providers.provider_number
		isPassing = True
		# Get the size of the providers dictionary:
		dictionary_size = len(Providers.providers)
		print(f"Running REQUEST and REGEX source checks with '{testTickerSymbol}' symbol\n")
		for i in range(dictionary_size):
			# The first try: except: block tests out the request to the actual URL:
			testURL = list(Providers.providers.keys())[i] + str(testTickerSymbol)
			# this tells us globally which provider to use, so we are changing it for each iteration:
			Providers.provider_number = i
			
			print("TESTING SOURCE NUMBER " + str(i) + "... (" + testURL + ")")

			try:
				# Try for the request:
				req = Request(
					url=list(Providers.providers.keys())[Providers.provider_number] + str(testTickerSymbol), 
					headers={'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0"}
				)
		
				#Get the source in string format:
				source = str(urlopen(req).read())
				print("REQUEST check for Source number " + str(i) + " is working.")
				# The second try: except: block tests out the regex pattern:
				try:
					
					gatherInfo.gatherPrice(source)
					print(f"REGEX check for Source number {i} is working.\n")
				except:
					print(f"REGEX check for Source number {i} is NOT working.\n")
					isPassing = False
			except:
				print(f"REQUEST check for Source number {i} is NOT working.\n")
				isPassing = False
		if isPassing:
			print("All providers are working.\n")
		else:
			print("\nSome providers are not working. Verify that the ticker symbol is valid, or create an issue if persistent.\n")
			if exitOnFailure:
				print("\nexitOnFailure is set to True. Exiting...")
				exit()
		# Return the source number to its original value:
		Providers.provider_number = temp_provider_number
		return isPassing
	# Function that tests the selected provider specified by the provider_number variable:
	def testSelectedProvider(testTickerSymbol = "AMZN"):
		isPassing = True
		# Get the URL and the regex of the selected provider:
		try:
			# Try for the request:
			req = Request(
				url=list(Providers.providers.keys())[Providers.provider_number] + str(testTickerSymbol), 
				headers={'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0"}
			)
	
			#Get the source in string format:
			source = str(urlopen(req).read())
			
		except:
			isPassing = False

		# The second try: except: block tests out the regex pattern:
		try:
			# Test out the regex:
			gatherInfo.gatherPrice(source)
		except:
			isPassing = False

		return isPassing
class gatherInfo:
	
	#Get the source:
	def getSource(stockSymbol, proxy = ""):
		# Add a new fail-safe mechanism here. This also goes in the gatherSourchWithUserAgent function, and the getPrice function will have a regex check rather than a requeset check.
		failed_providers = []
		# Initial proxy support (to be tested):
		# if proxy:
		# 	try:
		# 		# Initial Proxy Support:
		# 		proxy_support = urllib.request.ProxyHandler({'http': 'http://' + proxy, 'https': 'https://' + proxy})
		# 		opener = urllib.request.build_opener(proxy_support)
		# 		urllib.request.install_opener(opener)
		# 	except:
		# 		print("ERR: Could not set up proxy support.")
		#Add a while True: loop here. If the first try: block below succeeds, the while loop will break due to the 'return source' line.
		while True:
			try:
				# Here, instead of defaulting to random user agents/not having a user agent at all, we are use a fixed user agent!!!
				req = Request(
					url=list(Providers.providers.keys())[Providers.provider_number] + str(stockSymbol), 
					headers={'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0"}
				)

				#Get the source in string format:
				source = str(urlopen(req).read())
				# Also test out the gathering of the price (this tests out the regex pattern for that provider):
				gatherInfo.gatherPrice(source)
				
				#If everything goes fine, then source will be returned:
				return source
			except:
				# Here, check whether or not the provider is working first to check if the provider is the problem. If the provider did fail, switch the provider, and attempt to get the source once again.
				if not Providers.testSelectedProvider():
					# Perhaps here add an if statement to check whether or not the failed provider list (imported either from a paremeter or found in the Providers class) is included in the failed provider list.
					print(f"ERR: Provider {Providers.provider_number} failed. Switching to a different provider...")
					# Append the failed provider number to the failed_providers:
					failed_providers.append(Providers.provider_number)
					while Providers.provider_number in failed_providers:
						# Check if the failed_providers list is the same amount as the actual providers amount, if it is, it means all providers failed.
						if (len(failed_providers) != len(Providers.providers)):
							Providers.provider_number = random.randint(0, len(Providers.providers)-1)
						else:
							raise Exception(f"\nAll providers seemed to have failed while trying to make a request. Please create an issue if persistent. Try to use API.getPriceCNBCAPI('{stockSymbol}') instead.")
				# If the provider is not the issue, then it is the ticker/stock symbol that is not valid:			
				else:
					#If the inputted company/stock symbol is invalid, then an exception will occur:
					raise Exception(f"ERR: Could not find symbol/company through source {Providers.provider_number}'s indexes.")
			
	# Function that extracts the price based on the passed down source code:
	def gatherPrice(source):
		
		# Get the regex pattern based on the provider_number:
		regex_pattern = list(Providers.providers.values())[Providers.provider_number]
		
		# Main regex to find it all :)
		price = re.findall(regex_pattern, source)
		counter = 0
		# Avoid any strings in case the regex pattern finds other things beside the price:
		for i in range(len(price)):
			try:
				float(price[i])
				# Break out of the loop if the float is found:
				break
			except:
				counter += 1
		# Replace any commas in the found list from the "re" library:
		price = float(price[counter].replace(",", ''))
		
		return price
	
	#Allows for the making of requests with a user agent. 
	def getSourceWithUserAgent(stockSymbol, AgentPositionNumber, proxy = ""):
		
		#User agents list:
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
		
		#Get the user agent based on the number of the parameter "AgentPositionNumber":
		useragentpick = user_agents[AgentPositionNumber]

		#Initial proxy support (to be tested):
		# if proxy:
		# 	try:
		# 		# Initial Proxy Support:
		# 		proxy_support = urllib.request.ProxyHandler({'http': 'http://' + proxy, 'https': 'https://' + proxy})
		# 		opener = urllib.request.build_opener(proxy_support)
		# 		urllib.request.install_opener(opener)
		# 	except:
		# 		print("ERR: Could not set up proxy support.")

		failed_providers = []
		while True:
			try:
			#Make the request with user agent:
				req = Request(
					url=list(Providers.providers.keys())[Providers.provider_number] + str(stockSymbol), 
					headers={'User-Agent': useragentpick}
				)
			
				#Get the source in string format:
				source = str(urlopen(req).read())

				# Also test out the gathering of the price (this tests out the regex pattern for that provider):
				gatherInfo.gatherPrice(source)
				return source
			except:
				if not Providers.testSelectedProvider():
					# Perhaps here add an if statement to check whether or not the failed provider list (imported either from a paremeter or found in the Providers class) is included in the failed provider list.
					print(f"ERR: Provider {Providers.provider_number} failed. Switching to a different provider...")
					# Append the failed provider number to the failed_providers:
					failed_providers.append(Providers.provider_number)
					while Providers.provider_number in failed_providers:
						# Check if the failed_providers list is the same amount as the actual providers amount, if it is, it means all providers failed.
						if (len(failed_providers) != len(Providers.providers)):
							Providers.provider_number = random.randint(0, len(Providers.providers)-1)
						else:
							raise Exception(f"\nAll providers seemed to have failed while trying to make a request. Please create an issue if persistent. Try to use API.getPriceCNBCAPI('{stockSymbol}') instead.")
				else:
					# If the provider is not the issue, then it is the ticker/stock symbol that is not valid:			
					raise Exception(f"ERR: Could not find symbol/company through source {Providers.provider_number}'s indexes.")
				

#Set of tools that combine these two functions above together:
class Tools:
	#stockSymbol = company symbol (ticker symbol). Ex: "TSLA". type = str
	#iterations = Number of data samples to gather. type = int
	#randomUserAgent = use a random user agent out of 24 user agents. type = bool
	#breakInterval = time between each data sample gathered, default is 5 seconds (Lowering this could result in duplicate values). type = int
	#antiBan = Randomizes request time, making it less suspicious that the requests are automated. type = bool
	#printOUTPUT = print each stock value every iteration. type = bool
	#returnTimeSpent = Returns the total time spent at gathering the samples. type = bool
	
	#Get multiple prices:
	def multiDataGathering(stockSymbol, iterations, breakInterval = 5, antiBan = False, randomUserAgent = False, printOUTPUT = False, returnTimeSpent = False):
		
		#Main price list:
		prices = []
		
		#Used to store time spent values:
		randomDelays = []

		for i in range(iterations):
			#Check if antiBan is active:
			if antiBan == True:
				#Anti ban, generates random time request:
				randomdelay = (random.randint(50,100))/100
				#append the random delay value
				randomDelays.append(randomdelay)
				time.sleep(randomdelay)
				#Gather the source:
			
			if randomUserAgent == True:
				#generate random number to pick a random user agent:
				randomagentnumber = random.randint(0,24)
				source = gatherInfo.getSourceWithUserAgent(stockSymbol, randomagentnumber)
			elif randomUserAgent == False:
				# The getSource actually checks for provider integrity/fails.
				source = gatherInfo.getSource(stockSymbol)
				
			#Gather the price based on the source:
			price = gatherInfo.gatherPrice(source)
			#append the info:
			prices.append(price)
			#Check if the printed output option is active:
			if printOUTPUT == True:
				print(price)
			#Sleep for the breakinterval time:
			
			#Does not count the last time.sleep if the last iteration finished processing the last request.
			if (iterations-1) != i:
				time.sleep(breakInterval)
			
			
		#Return the values:
		if returnTimeSpent == True and antiBan == True:
			#Adds all of the spent time gathering the data together:
			timeSpent = (iterations * breakInterval) + sum(randomDelays)
			return prices, timeSpent
		elif returnTimeSpent == True and antiBan == False:
			timeSpent = (iterations * breakInterval)
			return prices, timeSpent
		else:
			
			#If neither the antiBan or the returnTimeSpent are used, then no time will be calculated and only prices will be returned.
			return prices
		
		
	#Get a single price:
	def getSinglePrice(stockSymbol, randomUserAgent = False):

		#Check if the parameter "randomUserAgent" is set to True or False:
		if randomUserAgent == True:
			#generate random number to pick a random user agent:
			randomagentnumber = random.randint(0,24)
			source = gatherInfo.getSourceWithUserAgent(stockSymbol, randomagentnumber)
		elif randomUserAgent == False:
			source = gatherInfo.getSource(stockSymbol)
		price = gatherInfo.gatherPrice(source)
		
		return price
	
	#Get the trend of the data data: returnChange is set to False. If set to true, the first value will be subtracted from the last to see the difference in change.
	def getTrend(pricesList, returnChange = False):
		Trend = ''
		#Get the amount of prices:
		amountPrices = len(pricesList)
		#Get the first price:
		firstPrice = pricesList[0]
		#Get the last price:
		lastPrice = pricesList[amountPrices - 1]
		
		#Compare the two prices:
		if firstPrice < lastPrice:
			Trend = 'up'
		elif firstPrice > lastPrice:
			Trend = 'down'
		else:
			Trend = 'neutral'
		
		if returnChange == True:
		#Return the value of trend as a string.
			Change = float(lastPrice) - float(firstPrice)
			return Trend, Change
		else:
			return Trend
		
	def saveDataToFile(data,  saveFilePath, timeSpent = 0, trend = ''):
		
		#turn parametric data into string types to allow concatination in writing of data:
		data = str(data)
		
		saveDataFileName = "stockstirSaveData.txt"
		
		#Here, removee last slash mark or space if there is one:
		position = 1
		while True:
			lastcharacter = saveFilePath[-position]
			if lastcharacter == "/" or lastcharacter == ' ':
				saveFilePath = saveFilePath[:-position]
			else:
				break
		
		#Open new file:
		f = open(saveFilePath + "/" + saveDataFileName, 'a')
		
		#Here, write the contents of the data:
		
		#Get the current time:
		current_time = time.ctime()
		
		f.write("\n\n" + current_time + "\nData: " + data)
		
		#Check parameters and write whther true or false
		if timeSpent == 0:
			f.write("\nTime Spent: undefined")
		elif timeSpent != 0:
			timeSpent = str(timeSpent)
			f.write("\nTime Spent: " + timeSpent)
		if trend == '':
			f.write("\nTrend: undefined")
		elif trend != '':
			f.write("\nTrend: " + trend)
		#Close the file:
		f.close()
# Thank you for suggesting API support! (still in early stages)
class API:
	#API class that allows for the gathering of data from the internet through APIs.
	
	# Initial implementation of the Alpha Vantage API:
	def getAlphaVantageData(stockSymbol, apiKey, type = 'TIME_SERIES_INTRADAY'):
		# Get the URL for the API:
		url = 'https://www.alphavantage.co/query?function=' + type +'&symbol=' + stockSymbol + '&interval=5min&apikey=' + apiKey
		r = requests.get(url)
		data = r.json()
		return data
	
	# For the CNBC 'API' json structure. This is not an actual API, but rather a JSON structure that is used to get various information on a company stock.
	# Thank you Gr1pp717 (https://www.reddit.com/user/Gr1pp717/) for the research and resources used in the methods below!
	def getCNBCAPIJSONData(stockSymbol):
		CNBC_API_URL = 'https://quote.cnbc.com/quote-html-webservice/restQuote/symbolType/symbol?symbols=' + stockSymbol
		r = requests.get(CNBC_API_URL)
		data = r.json()
		return data
	def listCNBCData(stockSymbol):
		data = API.getCNBCAPIJSONData(stockSymbol)
		formatted_dictionary_data = data['FormattedQuoteResult']['FormattedQuote'][0]
		keys = list(formatted_dictionary_data.keys())
		values = list(formatted_dictionary_data.values())
		for i in range(len(keys)):
			print(f"Index Value: {i}. {keys[i]}: {values[keys.index(keys[i])]}")
		return keys, values
	# Get a single price using the CNBC 'API'
	def getPriceCNBCAPI(stockSymbol):
		data = API.getCNBCAPIJSONData(stockSymbol)
		price = data['FormattedQuoteResult']['FormattedQuote'][0]['last']
		return price