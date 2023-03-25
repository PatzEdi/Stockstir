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

class gatherInfo:
	#Get the source:
	def getSource(stockSymbol):
		try:
			request_url = urllib.request.urlopen("https://www.cnbc.com/quotes/" + str(stockSymbol))
			source = str(request_url.read())
			
			#If everything goes fine, then source will be returned:
			return source
		except:
			
			#If the inputted company/stock symbol is invalid, then an exception will occur:
			raise Exception("ERR: Could not find symbol/company through CNBC indexes.")
			
		
	def gatherPrice(source):
		
		#Main regex to find it all :)
		price = re.findall('(?<="price":")(.*)(?=","priceChange":")', source)
		
		#Replace any commas in the found list from the "re" library:
		
		price = float(price[0].replace(",", ''))
		
		return price
	
	#Allows for the making of requests with a user agent. 
	def getSourceWithUserAgent(stockSymbol, AgentPositionNumber):
		
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
		
		try:
		#Make the request with user agent:
			req = Request(
				url="https://www.cnbc.com/quotes/" + str(stockSymbol), 
				headers={'User-Agent': useragentpick}
			)
		
			#Get the source in string format:
			source = str(urlopen(req).read())
			
		except:
			
			#If the inputted company/stock symbol is invalid, then an exception will occur:
			raise Exception("ERR: Could not find symbol/company through CNBC indexes.")
			
		
		return source
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
