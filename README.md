# Stockstir
Instantly and easily gather stock data in real time of any company in any of your python scripts

![stockstir-logo](https://user-images.githubusercontent.com/116693779/227736659-b39d549e-ccfd-4bef-851e-228f5bb6ac02.jpg)

<p align="center">
	<img src="https://img.shields.io/badge/License-MIT-brightgreen"
		height="23">
	<img src="https://img.shields.io/badge/Creator-PatzEdi-brightgreen"
		height="23">
	<img src="https://img.shields.io/badge/Version-Latest-brightgreen"
		height="23">
</p>

## **Important Note:**

**The full documentation for this library is now hosted on readthedocs.org! [ReadtheDocs Documentation](https://stockstir.readthedocs.io/en/latest/index.html) file under the project files. Take a look to explore the features of Stockstir and how to use them, as well as getting to know how Stockstir works in a detailed way.**

## **Made with Python, made with passion: Stockstir is a way to gather stock data from any Python script in an easy and quick way.** 
____________________________________________________________________________
## **CHANGELOG: 1.0.2**
- Added documentation to readthedocs.org. Now, the documentation is much easier to access and read through!

## **Usage**

Installation:
```
pip install Stockstir
```

Importing:
```
import Stockstir
```
Simple example to gather stock data from any website:
```
Stockstir.Tools.getSinglePrice("ticker/stockSymbol")
```
Since this library has many more features (too many to explain here in a neat way), you can take a look at the [Documentation](https://stockstir.readthedocs.io/en/latest/index.html) file under the project files.

## **Features**
- Instantly gather stock prices from any company in real time.
- Includes a single price gathering tool to get the price of any company once.
- Includes a multi data gathering tool which has features like anti ban, random user agents, delay for each request, and of course how much data to gather.  
- Useful tools such as getting the trend of the gathered data determining whether the stock price went up, down, or stayed neutral throughout that time period.
- Ability to return the time spent in the total process of gathering the data. This can be useful in order to analyze data and comparing it to the time spent overall. Not only that, but getting the trend also comes with an optional option to get the change between the first and the last value of the gathered data.
- Includes a useful tool to create logs of the data gathered if needed, and does so by writing the data in a neat way to a file at a specified directory of your choice.
- Includes the ability to make requests with random user agents (up to 24 different agents).
- Very easy to use.
- In case you accidentally put the wrong ticker/stock symbol as a parameter, an exception will occur and warns of the incorrect input.
- Fast and efficient, no time to waste. Stockstir will save you time.
- In terms of code... Comments are included to guide you through what the script does. The code is split into two classes: The Tools class and the gatherInfo class. The only ones you really need are under the Tools class, as the Tools class combines what is in the gatherInfo class to make a complete set of tools.
____________________________________________________________________________
## **Why?**
- Gathering stock data is definitely something that can be useful to many in their Python scripts. 
- Real time stock data can be used to look at a specific price of any company and determine what to do with that data later on. For example, if you wanted to get notified one the price of stock goes above or below a value, it is now easier than ever to do something like that. 
____________________________________________________________________________
## **How?**
- Using many useful libraries (credits below), I was able to get what I needed to make a library like this one. 
- The way it works is very interesting. I basically gathered the source code of the webpage of CNBC and added to the url of "https://www.cnbc.com/quotes/" the ticker/stock symbol. I made a request to that URL, got the source code, and created a regex pattern that suited the website CNBC. I figured out that the regex pattern I used was universal for any company and its source at CNBC. Using the regex, I could instantly find the value of the price. So overall, this script basically sends a request to CNBC and analyzes the source in order to gather the price.
____________________________________________________________________________
## **User notice**
- Please be aware that using a rotating IP address (for example a VPN with a rotating IP) could help you not get banned from the website CNBC when making a lot of requests. If you want to use the multi data gathering tool, you can use the anti ban function to try to avoid getting banned from the website and being recognized as a potential "bot" making automatic requests.
- This project is still a work in progress. Adding new features is very easy, but so far I have started with it simple. 
- Please note that the README file briefly goes into the details of how the project works. If you want more in depth details of what each and every function and parameter does, take a look at the [Documentation](https://stockstir.readthedocs.io/en/latest/index.html) file in the project files.
____________________________________________________________________________
## **Services used (Credits):**
- [Requests module](https://requests.readthedocs.io/en/latest/)
- [URLLib module](https://docs.python.org/3/library/urllib.html)
- [Re module](https://docs.python.org/3/library/re.html)
- [Time module](https://docs.python.org/3/library/time.html)
- [Random module](https://docs.python.org/3/library/random.html)

____________________________________________________________________________
## **Make sure to leave a star!**
- If you like this project, leaving a star is what motivates me in doing more. Thank you, and I hope this is useful in order to gather the stock data you need.
